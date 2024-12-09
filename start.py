import subprocess
import sys
import threading
import time
from datetime import datetime

import pyfiglet

import root
import step
import util.dataUtils as dataUtils
from util import adbUtils

print(pyfiglet.figlet_format("Auto - Ghost", font='slant'))

author = "作者: YBKIM"
version = "版本: 1.0.0"
# 打印封面
print("=" * 70)
print(f"{author:^70}")
print(f"{version:^70}")
print("=" * 70)



end_date ="2024-12-12"
if datetime.now() > datetime.strptime(end_date, "%Y-%m-%d"):
    # print("当前日期大于结束日期，程序结束。")
    sys.exit(0)
# if not dataUtils.check_device():
#     sys.exit(0)

# 初始化缓存库
dataUtils.clear_device()

# 启动adb wifi 服务
subprocess.run([adbUtils.adb_path, 'tcpip 5555'], capture_output=True)

# 监听USB
root_thread = threading.Thread(target=root.start)
root_thread.start()

# 监听WIFI链接
step_thread = threading.Thread(target=step.start)
step_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted. Exiting...")
