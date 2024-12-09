import os
import time

import uiautomator2 as u2

import action
import util.dataUtils as dataUtils
import util.deviceUtils as deviceUtils
from util import adbUtils
from util.adbUtils import adb_path


def start():
    while True:
        print("监控USB中....")
        devices = adbUtils.get_usb_device_serial()
        usb_devices = deviceUtils.check_usb(devices)
        if len(usb_devices) != 0:
            d = u2.connect(usb_devices)
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
            # 保存 ip
            dataUtils.save_device_ip(ip)
            print("激活成功请断开数据线")
        time.sleep(5)
