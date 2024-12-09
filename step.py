import time

import uiautomator2 as u2

import action
from util import dataUtils


def start():
    while True:
        devices = dataUtils.get_device_ips(0)
        for device in devices:
            current_ip = device['ip']
            try:
                print(f"尝试WIFI链接:{current_ip}")
                d = u2.connect(current_ip + ':5555')
                print(f"{current_ip}链接成功")
                d.press('home')
                dataUtils.random_sleep()
                step = action.Step(d)
                # 启动 app
                work_space = d(className='android.widget.RelativeLayout')
                for app in work_space:
                    if 'WA' in app.info['contentDescription'] or 'WhatsApp' in app.info['contentDescription']:
                        # 清理后台应用
                        step.clear_system_app()
                        # 初始化 IP
                        step.restart_network()
                        app.click()
                        user_list = dataUtils.get_user_list()
                        for i in range(user_list.nrows - 1):
                            user = user_list.row(i + 1)[0].value
                            try:
                                step.click_new_chat()

                                step.click_search_icon()
                                # 清空搜索输入框
                                step.clear_search_input()
                                # 粘贴
                                step.past_search_input(user)
                                # 点击用户
                                step.click_user(user)
                                message_list = dataUtils.get_message()
                                step.simulate_typo_voice()
                                for message in message_list:
                                    if message == 'gif':
                                        # 点击emoji icon
                                        step.click_emoji_icon()
                                        # 点击emoji
                                        step.click_emoji()
                                    else:
                                        # 输入信息
                                        step.past_message_input(dataUtils.simulate_typo(message))
                                        # 发送
                                        step.send_message()
                                # 返回
                                step.back_to_list()
                            except Exception as e:
                                d.press('back')
                                time.sleep(2)
                                d.press('back')
                                time.sleep(2)
                                d.press('back')
            except Exception as e:
                print(' 连接失败请重新激活')
                print(e)
        time.sleep(5)
