import os

import platform
import subprocess
import sys

os_name = platform.system()
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if getattr(sys, 'frozen', False):
    project_root = os.path.dirname(sys.executable)

adb_path = ""
if os_name == "Windows":
    adb_path = os.path.join(project_root, "lib/windows", "adb.exe")
elif os_name == "Darwin":
    adb_path = os.path.join(project_root, "lib/mac", "adb")


def get_usb_device_serial():
    # 执行 adb devices 命令
    result = subprocess.run([adb_path, 'devices'], capture_output=True, text=True)

    # 获取命令的输出
    output = result.stdout

    # 解析设备序列号
    devices = []
    for line in output.splitlines():
        if line.startswith('List'):
            continue
        if not line.strip().endswith('device'):
            continue

        device_info = line.split('\t')
        if len(device_info) > 1 and device_info[1] == 'device':
            serial_number = device_info[0]
            devices.append(serial_number)

    return devices
