import os

import platform
import sys

os_name = platform.system()
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# 如果是打包后的程序，使用 sys._MEIPASS 来访问临时目录
if getattr(sys, 'frozen', False):
    project_root = os.path.dirname(sys.executable)

adb_path = ""
if os_name == "Windows":
    adb_path = os.path.join(project_root, "platform-tools-windows", "adb.exe")
elif os_name == "Darwin":
    adb_path = os.path.join(project_root, "platform-tools-mac", "adb")

user_path = 'data/user.xlsx'
message_path = 'data/message.xlsx'