import threading
import time

from util import dataUtils, deviceUtils
import uiautomator2 as u2
from config.config import adb_path

# if not dataUtils.check_device():
#     print("该设备已到期")


d = u2.connect()


# d(resourceId = 'com.whatsapp:id/voice_note_btn').long_click(20)
# audio_path = '/autoGhostData/Mixdown.wav'

# d.shell(adb_path + ' am start -a android.intent.action.VIEW -d file://{audio_path} -t audio/wav')
d.shell(adb_path + ' shell mkdir -p /autoGhost')

# # 创建一个继承 Thread 的类
# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(5):
#             print(f"线程 {self.name} 正在运行... {i}")
#             time.sleep(1)
#
# # 创建并启动线程
# thread = MyThread()
# thread.start()
#
# # 主线程继续执行
# for i in range(5):
#     print(f"主线程正在运行... {i}")
#     time.sleep(1)
#
# # 等待线程结束
# thread.join()
#
# print("主线程和子线程都执行完毕")
