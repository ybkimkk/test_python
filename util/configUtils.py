def load_config(file_path):
    a = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):  # 跳过空行和注释
                key, value = line.split('=', 1)
                a[key.strip()] = value.strip()
    return a


read = load_config('config/config.txt')

config = {
    # app包
    "package": "com.whatsapp",
    # 搜索图标
    "searchIcon": "com.whatsapp:id/menuitem_search",
    # 搜索输入框
    "searchInput": "com.whatsapp:id/search_input",
    # 搜索用户列表
    "searchList": "com.whatsapp:id/result_list",
    # 消息输入框
    "messageInput": "com.whatsapp:id/entry",
    # 发送按钮
    "messageSend": "com.whatsapp:id/send",
    # 表情图标
    "emojiIcon": "com.whatsapp:id/emoji_picker_btn",
    # gif分支
    "gifButton": "com.whatsapp:id/gifs",
    # gif列表区
    "gifArea": "com.whatsapp:id/search_result_view",
    # 语音按钮
    "voiceButton": "com.whatsapp:id/voice_note_btn",
    # 错字概率
    "errMsgRate": read['err_msg_rate'],
    # 误触语音概率
    "errVoiceRate": read['err_msg_rate'],
    # 最大停顿时间
    "sleepMax": read['sleep_max'],
}
