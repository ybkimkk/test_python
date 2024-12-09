

import action


import uiautomator2 as u2
d = u2.connect()
action =  action.Step(d)
# action.past_search_input('阿彬')
action.click_user('阿彬')