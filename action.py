from time import sleep

from conda_env.cli.main_update import description

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


def restart_network(d):
    screen_size = d.window_size()
    width, height = screen_size
    start_x = width - 100
    end_y = height // 8
    d.swipe(start_x, 0, start_x, end_y, duration=0.2)
    sleep(2)
    d(description='飞行模式,关闭').click()
    sleep(2)
    d(description='飞行模式,开启').click()
    sleep(3)
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


def click_user(d, user):
    elements = d(resourceId="com.whatsapp:id/conversations_row_contact_name")
    for element in elements:
        if element.exists:
            if user == element.get_text():
                element.click()
                break
    sleep(2)

def past_message_input(d):
    message_input = d(resourceId="com.whatsapp:id/entry")
    sleep(2)
    message_input.click()
    sleep(2)
    message_input.clear_text()
    sleep(2)
    message_input.set_text("aaaaaaaaaa?")


def send_message(d):
    sleep(2)
    d(resourceId="com.whatsapp:id/send").click()


def back_to_list(d):
    d.press("back")
    sleep(2)
    d.press("back")