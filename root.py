import os
import sys

import uiautomator2 as u2

import action
import util.dataUtils as dataUtils
import util.deviceUtils as deviceUtils
from util import adbUtils
from util.adbUtils import adb_path

if not dataUtils.check_device():
    sys.exit(0)

devices = adbUtils.get_usb_device_serial()
usb_devices = deviceUtils.check_usb(devices)
if len(usb_devices) == 0:
    print("请用USB方式连接手机")
    sys.exit(0)

d = u2.connect(usb_devices)
os.system(adb_path + ' devices')
# 授权
action.mobile_root(d)
# 检查是否已启动 Wi-Fi 模式
netstat_output = d.shell("netstat -an | grep ':5555' | wc -l")
netstat_count = int(netstat_output.output.strip())

if netstat_count == 0:
    d.shell(adb_path + ' tcpip 5555')
# 获取 ip
config = d.shell("ifconfig wlan0")
ip = dataUtils.extract_ip(config.output)
if int(netstat_output.output) == 1:
    dataUtils.clear_ip()
# 保存 ip
dataUtils.save_device_ip(ip)
print("激活成功请断开数据线")
