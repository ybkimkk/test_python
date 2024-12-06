import random

import uiautomator2 as u2

import action
from util import dataUtils, configUtils
from util.configUtils import config

d = u2.connect()


# d(resourceId = 'com.whatsapp:id/voice_note_btn').long_click(20)
# audio_path = '/autoGhostData/Mixdown.wav'


#
action.past_search_input(d, "asd?")
