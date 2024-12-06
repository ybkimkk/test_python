import uiautomator2 as u2

import action
import util.dataUtils as dataUtils

if not dataUtils.check_device():
    print("该设备已到期")
else:
    # wifi 连接
    try:
        print("尝试WIFI链接")
        d = u2.connect(dataUtils.get_device_ip() + ':5555')
        print("链接成功")
    except Exception as e:
        print('wifi 连接失败请重新激活')
        print(e)
        # sys.exit(1)

    # 清理后台应用
    action.clear_system_app(d)
    # 启动 app
    action.app_start(d)
    user_list = dataUtils.get_user_list()
    for i in range(user_list.nrows - 1):
        try:
            action.click_search_icon(d)
            user = user_list.row(i + 1)[0].value
            print(f"第{i + 1}条数据,用户名:[{user}],开始执行")
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
