from time import sleep

from config.config import adb_path


def mobile_root(d):
    d.shell(adb_path + ' root')
    d.shell(adb_path + ' shell pm grant com.android.shell android.permission.INJECT_EVENTS')


def app_start(d):
    d.shell('am start -n com.whatsapp/.Main')
    while True:
        current_app = d.app_current()
        if current_app.get('package') == "com.whatsapp":
            print("WhatsApp 已启动完成")
            break
        print("等待 WhatsApp 启动...")
        sleep(1)


def click_search_icon(d):
    while not d(resourceId="com.whatsapp:id/menuitem_search").exists:
        print("等待搜索图标...")  # 如果元素不存在则等待
        sleep(1)
    d(resourceId="com.whatsapp:id/menuitem_search").click()


def clear_search_input(d):
    while not d(resourceId="com.whatsapp:id/search_input").exists:
        print("等待搜索框...")  # 如果元素不存在则等待
        sleep(1)
    d(resourceId="com.whatsapp:id/search_input").clear_text()


# 循环等待 "search_input" 元素再次可用
def past_search_input(d, user):
    sleep(1)
    d(resourceId="com.whatsapp:id/search_input").set_text(user)


# def restart_network(d):
#     d(resourceId="com.whatsapp:id/contact_row_container").


def click_user(d):
    d.press("home")
    sleep(1)
    d.press("recent")
    sleep(1)
    d(resourceId="com.miui.home:id/clearAnimView").click()
    sleep(1)
    d.press("home")
    sleep(1)


def clear_system_app(d):
    d.press("home")
    sleep(1)
    d.press("recent")
    sleep(1)
    d(resourceId="com.miui.home:id/clearAnimView").click()
    sleep(1)
    d.press("home")
    sleep(1)
