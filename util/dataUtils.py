import re
import time
import random

import xlrd

from config.config import user_path
from config.config import message_path


def save_device_ip(ip):
    with open('data/device_ip.txt', 'w') as f:
        f.write(f"{ip}")
    print('设置成功,请断开数据线')

def get_device_ip():
    with open('data/device_ip.txt', 'r') as f:
        return f.read()

def extract_ip(output):
    match = re.search(r'inet addr:(\d+\.\d+\.\d+\.\d+)', output)
    if match:
        return match.group(1)
    else:
        return None
def random_sleep():
    time.sleep(random.randint(2,5))

def get_user_list():
    user = xlrd.open_workbook(user_path)
    return  user.sheets()[0]

def get_message():
    message = xlrd.open_workbook(message_path)
    message_sheets =  message.sheets()[0]
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
    # for phrase in selected_phrases:
    #     print(phrase)
