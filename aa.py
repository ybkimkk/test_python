import time
from time import sleep

import uiautomator2 as u2


def app_start(d):
    d.shell('adb root')
    d.shell('adb shell pm grant com.android.shell android.permission.INJECT_EVENTS')
    device.press("home")
    sleep(1)
    device.press("recent")
    sleep(1)
    device(resourceId="com.miui.home:id/clearAnimView").click()
    sleep(1)
    device.press("home")
    sleep(1)
    d.shell('am start -n com.whatsapp/.Main')

    while True:
        current_app = d.app_current()
        print(current_app)
        if current_app.get('package') == "com.whatsapp":
            print("WhatsApp 已启动完成")
            break
        print("等待 WhatsApp 启动...")
        time.sleep(1)

def click_search_icon(d):
    while not d(resourceId="com.whatsapp:id/menuitem_search").exists:
        print("等待搜索框...")  # 如果元素不存在则等待
        time.sleep(1)
    d(resourceId="com.whatsapp:id/menuitem_search").click()


def clear_search_input(d):
    while not d(resourceId="com.whatsapp:id/search_input").exists:
        print("等待搜索框...")  # 如果元素不存在则等待
        time.sleep(1)
    d(resourceId="com.whatsapp:id/search_input").clear_text()


# 循环等待 "search_input" 元素再次可用
def past_search_input(d):
    sleep(1)
    d(resourceId="com.whatsapp:id/search_input").set_text("中午吃什么")


device = u2.connect()  # connect to device
app_start(device)
click_search_icon(device)
clear_search_input(device)
past_search_input(device)
print(device.dump_hierarchy())

