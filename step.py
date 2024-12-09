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
                print("尝试WIFI链接:" + current_ip)
                d = u2.connect(current_ip + ':5555')
                print(current_ip + "链接成功")
                d.press('home')
                dataUtils.random_sleep()
                # 启动 app
                work_space = d(className='android.widget.RelativeLayout')
                for app in work_space:
                    if 'WA' in app.info['contentDescription'] or 'WhatsApp' in app.info['contentDescription']:
                        # 清理后台应用
                        action.clear_system_app(d)
                        # 初始化 IP
                        action.restart_network(d)
                        app.click()
                        user_list = dataUtils.get_user_list()
                        for i in range(user_list.nrows - 1):
                            user = user_list.row(i + 1)[0].value
                            try:
                                action.click_new_chat(d)

                                action.click_search_icon(d)
                                # 清空搜索输入框
                                action.clear_search_input(d)
                                # 粘贴
                                action.past_search_input(d, user)
                                # 点击用户
                                action.click_user(d, user)
                                message_list = dataUtils.get_message()
                                action.simulate_typo_voice(d)
                                for message in message_list:
                                    if message == 'gif':
                                        # 点击emoji icon
                                        action.click_emoji_icon(d)
                                        # 点击emoji
                                        action.click_emoji(d)
                                    else:
                                        # 输入信息
                                        action.past_message_input(d, dataUtils.simulate_typo(message))
                                        # 发送
                                        action.send_message(d)
                                # 返回
                                action.back_to_list(d)
                            except Exception as e:
                                print(f"第{i + 1}条数据,用户名:[{user}],异常跳过")
                                print(e)
            except Exception as e:
                print(' 连接失败请重新激活')
                print(e)
        time.sleep(5)