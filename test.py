from util import dataUtils

# d = u2.connect()
# d.press('home')

# d(resourceId = 'com.whatsapp:id/voice_note_btn').long_click(20)
# audio_path = '/autoGhostData/Mixdown.wav'


# work_space =  d(className = 'android.widget.RelativeLayout')
# for app in work_space:
#     if 'WA' in app.info['contentDescription'] or  'WhatsApp' in app.info['contentDescription']:
#         app.click()
#         sleep(10)

# print(dataUtils.get_device_ip())


# dataUtils.save_device_ip('111')
# dataUtils.clear_ip()

current_ip = dataUtils.get_device_ips()
print(current_ip)
