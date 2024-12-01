import os

import uiautomator2 as u2

import action
import util.dataUtils as dataUtils

#初始化服务
os.system('adb kill-server')
os.system('adb start-server')
#USB 连接
d = u2.connect()
#授权
action.mobile_root(d)
#初始化 IP
action.restart_network(d)
#启动 wifi 模式
d.shell('adb tcpip 5555')
#获取 ip
config = d.shell("ifconfig wlan0")
ip = dataUtils.extract_ip(config.output)
#保存 ip
dataUtils.save_device_ip(ip)
