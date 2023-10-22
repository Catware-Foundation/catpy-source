# CatOS-Type Package
author = "aGrIk"
mode = "="
deps = 'None'
identificator = 'lyrics'
command_ru = 'текст'
description = 'Поиск текста песни в базе данных Genius.'

try:
    if parameter == "" and len(event.object["attachments"]) > 0:
        if event.object["attachments"][0]["type"] == "audio":
            audio = event.object["attachments"][0]["audio"]
            song = genius.search_song(audio["artist"], audio["title"])
            message("Текст песни " + song.artist + " - " + song.title + ":\n\n" + song.lyrics.replace("EmbedShare Url:CopyEmbed:Copy", "").replace("2EmbedShare URLCopyEmbedCopy", ""), reply=True)
            del audio
            del song
        else:
            message("Чтобы найти текст песни, нужно приложить к сообщению саму песню либо написать её название в том же сообщении.", reply=True)
    elif parameter == "":
        message("Чтобы найти текст песни, нужно приложить к сообщению саму песню либо написать её название в том же сообщении.", reply=True)
    else:
        song = genius.search_song(parameter)
        message("Текст песни " + song.artist + " - " + song.title + ":\n\n" + song.lyrics.replace("EmbedShare Url:CopyEmbed:Copy", ""), reply=True)
        del song
except:
    message("Текст не обнаружен.", reply=True)

