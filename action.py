import random
from time import sleep

from config.config import adb_path

import util.dataUtils as dataUtils


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
        sleep(2)


def click_search_icon(d):
    while not d(resourceId="com.whatsapp:id/menuitem_search").exists:
        print("等待搜索图标...")  # 如果元素不存在则等待
        dataUtils.random_sleep()
    d(resourceId="com.whatsapp:id/menuitem_search").click()


def clear_search_input(d):
    while not d(resourceId="com.whatsapp:id/search_input").exists:
        print("等待搜索框...")  # 如果元素不存在则等待
        dataUtils.random_sleep()
    d(resourceId="com.whatsapp:id/search_input").clear_text()


# 循环等待 "search_input" 元素再次可用
def past_search_input(d, user):
    dataUtils.random_sleep()
    d(resourceId="com.whatsapp:id/search_input").set_text(user)


def restart_network(d):
    screen_size = d.window_size()
    width, height = screen_size
    start_x = width - 100
    end_y = height // 8
    d.swipe(start_x, 0, start_x, end_y, duration=0.2)
    dataUtils.random_sleep()
    d(description='飞行模式,关闭').click()
    dataUtils.random_sleep()
    d(description='飞行模式,开启').click()
    dataUtils.random_sleep()
    d.press("home")
    dataUtils.random_sleep()


def clear_system_app(d):
    d.press("home")
    sleep(2)
    d.press("recent")
    sleep(2)
    d(resourceId="com.miui.home:id/clearAnimView").click()
    sleep(2)
    d.press("home")
    sleep(2)


def click_user(d, user):
    elements = d(resourceId="com.whatsapp:id/conversations_row_contact_name")
    for element in elements:
        if element.exists:
            if user in element.get_text():
                element.click()
                break
    dataUtils.random_sleep()


def past_message_input(d, message):
    message_input = d(resourceId="com.whatsapp:id/entry")
    dataUtils.random_sleep()
    message_input.click()
    dataUtils.random_sleep()
    message_input.clear_text()
    dataUtils.random_sleep()
    message_input.set_text(message)


def send_message(d):
    dataUtils.random_sleep()
    d(resourceId="com.whatsapp:id/send").click()


def back_to_list(d):
    d.press("back")
    dataUtils.random_sleep()
    d.press("back")


def click_emoji_icon(d):
    dataUtils.random_sleep()
    d(resourceId="com.whatsapp:id/emoji_picker_btn").click()
    dataUtils.random_sleep()
    d(resourceId="com.whatsapp:id/gifs").click()
    dataUtils.random_sleep()
    d(resourceId="com.whatsapp:id/video_preview_container").click()


def click_emoji(d):
    try:
        gif = d(resourceId="com.whatsapp:id/search_result_view")
        gif_area = gif.bounds()
        screen_size = d.window_size()
        width, height = screen_size
        d.swipe(500, height - 100, 500, gif_area[1])
        gif.child(index=random.randint(1, 5)).click()
    except Exception as e:
        print(e)
        click_emoji(d)
