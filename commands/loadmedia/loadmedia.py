# CatOS-Type Package
ret = ""
for audio in event.object["attachments"]:
    try:
        if audio["type"] == "audio":
            if ".mp3" in audio["audio"]["url"]:
                ret += f'Трек: {audio["audio"]["artist"]} - {audio["audio"]["title"]}, ссылка: {audio["audio"]["url"]}\n'
            else:
                ret += f'Трек: {audio["audio"]["artist"]} - {audio["audio"]["title"]}, невозможно получить ссылку\n'
        elif audio["type"] == "audio_message":
            ret += f'Голосовое: {audio["audio_message"]["link_mp3"]}\n'
    except:
        pass

for aye in event.object["fwd_messages"]:
    for audio in aye["attachments"]:
        try:
            if audio["type"] == "audio_message":
                ret += f'Голосовое: {audio["audio_message"]["link_mp3"]}\n'
        except:
            pass


if ret:
    #ret += "\nНам очень жаль, но теперь мы не можем получать для вас ссылки на треки из сообщений ВКонтакте. Чтобы узнать больше, прочтите наш пост: vk.com/wall-176186185_3434"
    message(ret)
else:
    if not event.from_chat:
        message("Ничего не найдено.")
    else:
        message("Ничего не найдено. Возможно, что это произошло из-за особенностей ВКонтакте, которые не позволяют команде работать в беседах должным образом.")
