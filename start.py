import action

import uiautomator2 as u2

d = u2.connect()  # connect to device
# d = u2.connect('device_ip')  # 如果是 Wi-Fi 连接


action.mobile_root(d)
action.clear_system_app(d)
action.restart_network(d)
action.app_start(d)
action.click_search_icon(d)
action.clear_search_input(d)
action.past_search_input(d)
print(d.dump_hierarchy())
