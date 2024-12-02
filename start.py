import sys
from time import sleep

import uiautomator2 as u2
import util.dataUtils as du
import action
import pandas as pd
import warnings
from config.config import file_path

# 禁用所有警告
warnings.filterwarnings('ignore')

# wifi 连接
try:
    d = u2.connect(du.get_device_ip() + ':5555')
except Exception as e:
    print('wifi 连接失败请重新激活')
    sys.exit(1)

#清理后台应用
action.clear_system_app(d)
# # 启动 app
action.app_start(d)

df = pd.read_excel(file_path)
for index, row in df.iterrows():
    print(f"第{index+1}条数据,用户名:[{row['用户名']}],开始执行")
    if index == 0:
        # 点击搜索
        action.click_search_icon(d)
    # 清空输入框
    action.clear_search_input(d)
    # 粘贴
    action.past_search_input(d, row['用户名'])
    # 点击用户
    action.click_user(d, row['用户名'])

    action.past_message_input(d)
