import os

import platform

os_name = platform.system()
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
adb_path = ""
if os_name =="Windows":
    adb_path = os.path.join(project_root, "platform-tools-windows", "adb.exe")
elif os_name == "Darwin":
    adb_path = os.path.join(project_root, "platform-tools-mac", "adb")

file_path = 'data/user.xlsx'