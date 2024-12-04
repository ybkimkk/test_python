import uiautomator2 as u2
import xlrd

import action
import util.dataUtils as dataUtils
from config.config import file_path

# # wifi 连接
try:
    print("尝试WIFI链接")
    d = u2.connect(dataUtils.get_device_ip() + ':5555')
    print("链接成功")
except Exception as e:
    print('wifi 连接失败请重新激活')
    print(e)
    # sys.exit(1)

# 清理后台应用
action.clear_system_app(d)
# 启动 app
action.app_start(d)
data = xlrd.open_workbook(file_path)
sheet1 = data.sheets()[0]
for i in range(sheet1.nrows):

    action.click_search_icon(d)
    sheet1_row_content = sheet1.row(i + 1)
    user = sheet1_row_content[0].value
    print(f"第{i + 1}条数据,用户名:[{user}],开始执行")
    # 清空搜索输入框
    action.clear_search_input(d)
    # 粘贴
    action.past_search_input(d, user)
    # 点击用户
    action.click_user(d, user)
    #输入信息
    action.past_message_input(d)
    #发送
    action.send_message(d)
    #返回
    action.back_to_list(d)