import threading
import time

import root
import step
import util.dataUtils as dataUtils

# if not dataUtils.check_device():
#     sys.exit(0)

#初始化缓存库
dataUtils.clear_device()
# 监听USB
root_thread = threading.Thread(target=root.start)
root_thread.start()

#监听WIFI链接
step_thread = threading.Thread(target=step.start)
step_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program interrupted. Exiting...")
