import http.client
import json
import random
import re
import time

import util.configUtils as configUtils
import util.deviceUtils as deviceUtils

import xlrd
import xlwt
import os

config = configUtils.config


def save_device_ip(ip):
    # 打开现有的Excel文件
    book = xlrd.open_workbook(config['deviceIpFile'])
    sheet = book.sheet_by_index(0)

    # 创建一个新的工作簿，用来写入更新的数据
    new_book = xlwt.Workbook()
    new_sheet = new_book.add_sheet('Sheet1')

    updated = False
    for row_idx in range(sheet.nrows):
        row = sheet.row_values(row_idx)

        if row[0] == ip:
            # 如果IP地址匹配，更新第二列的值为'0'
            for col_idx in range(sheet.ncols):
                if col_idx == 1:
                    new_sheet.write(row_idx, col_idx, 0)  # 更新第二列为 '0'
                else:
                    new_sheet.write(row_idx, col_idx, row[col_idx])  # 其他列保持不变
            updated = True
        else:
            # 如果IP地址不匹配，直接复制原始数据
            for col_idx in range(sheet.ncols):
                new_sheet.write(row_idx, col_idx, row[col_idx])

    # 如果没有更新任何行，说明没有找到该IP地址，需要追加新行
    if not updated:
        # 获取最后一行的位置
        new_row_idx = sheet.nrows
        # 插入新数据 (IP 地址为第一列，第二列为 '0')
        new_sheet.write(new_row_idx, 0, ip)
        new_sheet.write(new_row_idx, 1, '0')
        print(f"IP {ip} not found, added as a new entry.")

    # 保存更新后的Excel文件
    new_book.save(config['deviceIpFile'])

    if updated:
        print(f"IP {ip} updated with value '0' in second column.")


def get_device_ips():
    ip = xlrd.open_workbook(config['deviceIpFile'])
    ip_sheets = ip.sheets()[0]
    ip_list = []
    for row_idx in range(ip_sheets.nrows - 1, -1, -1):
        ip_list.append(ip_sheets.cell_value(row_idx, 0))
    return ip_list


def clear_ip():
    # 检查文件是否存在
    if not os.path.exists(config['deviceIpFile']):
        print("文件不存在！")
        return

    # 读取现有的 .xls 文件
    rb = xlrd.open_workbook(config['deviceIpFile'])
    ws = rb.sheets()[0]  # 获取第一个工作表

    # 创建新的工作簿
    wb = xlwt.Workbook()
    ws_new = wb.add_sheet('Sheet1')

    # 清空数据
    rows = ws.nrows
    for row_idx in range(rows):
        for col_idx in range(ws.ncols):
            ws_new.write(row_idx, col_idx, '')  # 清空单元格内容

    # 保存文件
    wb.save(config['deviceIpFile'])


def extract_ip(output):
    match = re.search(r'inet addr:(\d+\.\d+\.\d+\.\d+)', output)
    if match:
        return match.group(1)
    else:
        return None


def random_sleep():
    time.sleep(random.randint(2, int(config['sleepMax'])))


def get_user_list():
    user = xlrd.open_workbook(config['userDataFile'])
    return user.sheets()[0]


def get_message():
    message = xlrd.open_workbook(config['messageDataFile'])
    message_sheets = message.sheets()[0]
    phrases_dict = {}
    # 读取 Excel 数据并按数字分类
    for row_idx in range(1, message_sheets.nrows):  # 从第2行开始读取（跳过表头）
        number = message_sheets.cell_value(row_idx, 0)  # 获取数字列（第一列）
        phrase = message_sheets.cell_value(row_idx, 1)  # 获取话术列（第二列）

        if number not in phrases_dict:
            phrases_dict[number] = []
        phrases_dict[number].append(phrase)

    # 随机选择一个数字
    random_num = random.choice(list(phrases_dict.keys()))

    # 根据选中的数字获取话术列表
    selected_phrases = phrases_dict[random_num]

    # 打印选中的数字和对应的话术
    return selected_phrases


def simulate_typo(text):
    text = list(text)  # 将字符串转为字符列表，便于修改
    length = len(text)

    for i in range(length):
        # 决定是否插入错误
        if random.random() < float(config['errMsgRate']):
            error_type = random.choice(["swap", "delete", "insert"])

            if error_type == "swap" and i < length - 1:  # 字符交换
                # 随机交换当前字符和下一个字符
                text[i], text[i + 1] = text[i + 1], text[i]
            elif error_type == "delete":  # 删除字符
                text[i] = ""  # 删除当前字符
            elif error_type == "insert":  # 插入字符
                random_char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
                text.insert(i, random_char)
                i += 1
    return "".join(text)


def check_device():
    conn = http.client.HTTPConnection("localhost", 80)
    result = False
    try:
        # 请求头
        headers = {
            "Content-Type": "application/json",  # 指定内容类型为 JSON
        }
        # 请求体（参数）
        payload = {
            "deviceId": deviceUtils.get_machine_code()
        }
        conn.request("POST", "/api/checkDevice", body=json.dumps(payload), headers=headers)
        response = conn.getresponse()
        if response.status == 200:
            response_data = json.loads(response.read().decode())
            print(response_data.get('msg'))
            result = response_data.get('check')
            if not result:
                print("该设备已到期")
        else:
            print("服务器异常,请联系管理员")
            result = False
    except Exception as e:
        print(e)
    conn.close()
    return result
