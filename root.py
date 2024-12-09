import time

import uiautomator2 as u2

import action
import util.dataUtils as dataUtils
import util.deviceUtils as deviceUtils
from util import adbUtils


def start():
    while True:
        devices = adbUtils.get_usb_device_serial()
        usb_devices = deviceUtils.check_usb(devices)
        if len(usb_devices) != 0:
            print(f'检测到设备: {usb_devices}')
            d = u2.connect(usb_devices)
            step = action.Step(d)
            # 授权
            step.mobile_root()
            # 获取 ip
            config = d.shell("ifconfig wlan0")
            ip = dataUtils.extract_ip(config.output)
            # 保存 ip
            dataUtils.save_device_ip(ip)
            print(f"{usb_devices}激活成功,请断开数据线")
            while True:
                current_devices = adbUtils.get_usb_device_serial()
                if usb_devices not in current_devices:
                    break
                time.sleep(3)
        time.sleep(3)
