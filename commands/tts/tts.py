# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'tts'
command_ru = 'скажи'
description = 'Попросить сказать что либо'

try:
    if randd.randint(1, 100) == 10 and str(user_id) in ReadFF("usr/restricted.txt").split(","):
        Voice('usr/oral.ogg')
    else:
        if len(parameter) <= 1000 or str(user_id) in admins:
            voicemessage(parameter)
        else:
            message("Превышен порог в 1000 символов. Сократи свой текст.")
except:
    message("Похоже, что я не могу присылать тебе голосовые. Напиши мне в лс и я смогу прислать голосовое!")

    #upload_url = vk.docs.getMessagesUploadServer(type="audio_message", peer_id=peer_id)['upload_url']
    #request = requests.post(upload_url, files={'file': open('usr/speak.ogg', 'rb')}).json()
    #save = vk.docs.save(file=request['file'])['audio_message']
    #d = f'doc{save["owner_id"]}_{save["id"]}_{save["access_key"]}'
    #message(attachment=d, reply=True)

    #del tts
    #del upload_url
    #del request
    ##del save
    #del d
