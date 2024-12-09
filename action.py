import random
import re
import time

import util.adbUtils as adbUtils
import util.configUtils as configUtils
import util.dataUtils as dataUtils

config = configUtils.config


class Step:

    def __init__(self, d):
        self.d = d

    def mobile_root(self):
        self.d.shell(adbUtils.adb_path + ' root')
        self.d.shell(adbUtils.adb_path + ' shell pm grant com.android.shell android.permission.INJECT_EVENTS')
        self.d.shell(adbUtils.adb_path + ' shell settings put global airplane_mode_radios cell,bluetooth,nfc')

    def app_start(self):
        self.d.shell('am start -n com.whatsapp/.Main')
        while True:
            current_app = self.d.app_current()
            if current_app.get('package') == config['package']:
                break
            time.sleep(2)

    def click_new_chat(self):
        self.check_element_exist(self.d(resourceId=config['newChat']))
        self.d(resourceId=config['newChat']).click()

    def click_search_icon(self):
        self.check_element_exist(self.d(resourceId=config['searchIcon']))
        self.d(resourceId=config['searchIcon']).click()

    def clear_search_input(self):
        self.check_element_exist(self.d(resourceId=config['searchInput']))
        self.d(resourceId=config['searchInput']).clear_text()

    def past_search_input(self, user):
        self.check_element_exist(self.d(resourceId=config['searchInput']))
        self.input_msg(self.d(resourceId=config['searchInput']), user)

    def restart_network(self):
        screen_size = self.d.window_size()
        width, height = screen_size
        start_x = width - 100
        end_y = height // 8
        self.d.swipe(start_x, 0, start_x, end_y, duration=0.2)

        self.check_element_exist(self.d(description='飞行模式,关闭'))
        self.d(description='飞行模式,关闭').click()
        time.sleep(5)
        self.check_element_exist(self.d(description='飞行模式,开启'))
        self.d(description='飞行模式,开启').click()
        time.sleep(5)
        self.d.press("home")
        dataUtils.random_sleep()

    def clear_system_app(self):
        self.d.press("home")
        time.sleep(2)
        self.d.press("recent")
        time.sleep(2)
        self.d(resourceId="com.miui.home:id/clearAnimView").click()
        time.sleep(2)
        self.d.press("home")
        time.sleep(2)

    def click_user(self, user):
        self.check_element_exist(self.d(resourceId=config['searchList']))
        user = self.d(resourceId=config['searchList'])
        if '(You)' not in user.get_text():
            dataUtils.random_sleep()
            user.click()
            dataUtils.random_sleep()
        else:
            raise Exception()
    def past_message_input(self, message):
        self.check_element_exist(self.d(resourceId=config['messageInput']))
        message_input = self.d(resourceId=config['messageInput'])
        dataUtils.random_sleep()
        message_input.click()
        dataUtils.random_sleep()
        self.input_msg(message_input, message)

    def send_message(self):
        self.check_element_exist(self.d(resourceId=config['messageSend']))
        self.d(resourceId=config['messageSend']).click()

    def back_to_list(self):
        self.d.press("back")
        dataUtils.random_sleep()
        self.d.press("back")

    def click_emoji_icon(self):
        self.check_element_exist(self.d(resourceId=config['emojiIcon']))
        dataUtils.random_sleep()
        self.d(resourceId=config['emojiIcon']).click()
        self.check_element_exist(self.d(resourceId=config['gifButton']))
        dataUtils.random_sleep()
        self.d(resourceId=config['gifButton']).click()

    def click_emoji(self):
        try:
            gif = self.d(resourceId=config['gifArea'])
            gif_area = gif.bounds()
            screen_size = self.d.window_size()
            width, height = screen_size
            self.d.swipe(500, height - 100, 500, gif_area[1])
            gif.child(index=random.randint(1, 5)).click()
        except Exception as e:
            print(e)
            self.click_emoji()

    def simulate_typo_voice(self):
        err_rate = float(config['errVoiceRate'])
        if random.random() < err_rate:
            self.d(resourceId=config['voiceButton']).long_click(random.randint(2, 3))

    @staticmethod
    def input_msg(d, msg):
        result = re.findall(r'.', msg)
        m = ""
        for char in result:
            m = m + char
            d.send_keys(m)

    @staticmethod
    def check_element_exist(d):
        while not d.exists:
            dataUtils.random_sleep()
        if config['debug'] == '1':
            print(d.info)
