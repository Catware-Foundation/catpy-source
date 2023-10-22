# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'youtube'
command_ru = 'ютуб'
description = 'Ищет каналы и видео на видеохостинге YouTube. Укажите флаг "-видео" в конце для поиска видео'

channel = yt.search(q=parameter, type="channel", max_results=1)
try:
    channel_info = yt.get_channel_metadata(channel[0]["channel_id"])
except:
    channel_info = []

if len(channel) == 0 or len(channel_info) == 0 or "-видео" in parameter:
    parameter = parameter.replace(" -видео", "").replace("-видео ", "")
    vids = yt.search(q=parameter, max_results=10)

    if len(vids) > 0:
        yt_ret = f"По запросу \"{parameter}\" найдены следующие видео:\n\n"
        for vid in vids:
            yt_ret += f'▶ {vid["channel_title"]} — \"{vid["video_title"]}\"\nСмотреть: https://youtu.be/{vid["video_id"]}\n\n'
    else:
        yt_ret = "По вашему запросу не найдено ни одного видео."
else:
    yt_ret = f"Обнаружен YouTube-канал!\n\nНазвание: {channel_info['title']}\nСсылка: https://youtube.com/channel/{channel_info['channel_id']}\n"
    if channel_info["description"] != None: yt_ret +=  f"Описание: {channel_info['description']}\n\n"
    if channel_info['subscription_count']: yt_ret += f"{channel_info['subscription_count']} подписчиков\n"
    if channel_info["video_count"] != None: yt_ret +=  f"Выпущено: {channel_info['video_count']} видео\n"
    if channel_info['account_creation_date'] != None: yt_ret += f"Дата регистрации: {readableDate(channel_info['account_creation_date'])}\n"
    if channel_info['view_count'] != None: yt_ret += f"{channel_info['view_count']} просмотров\n"
    yt_ret += f"\nЕсли вы хотите найти видео по запросу \"{parameter}\", введите \"ютуб {parameter} -видео\""
message(yt_ret, reply=True)

#disable
