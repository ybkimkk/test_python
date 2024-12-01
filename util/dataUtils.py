import re


def save_device_ip(ip):
    with open('data/device_ip.txt', 'w') as f:
        f.write(f"{ip}")
    print('设置成功,请断开数据线')

def get_device_ip():
    with open('data/device_ip.txt', 'r') as f:
        return f.read()

def extract_ip(output):
    match = re.search(r'inet addr:(\d+\.\d+\.\d+\.\d+)', output)
    if match:
        return match.group(1)
    else:
        return None