# CatOS-type package
author = 'aGrIk'
mode = '='
deps = 'None'
identificator = 'ruletka'
command_ru = 'рулетка'
description = 'Пытается застрелить всех участников беседы, но убивает только одного. Есть более жестокий аналог: /чат рулетка'

if event.from_chat:
    hohlinki = []
    for ayeayeayeaye in vk.messages.getConversationMembers(peer_id=peer_id)["items"]:
        if ayeayeayeaye["member_id"] != -176186185:
            hohlinki.append(ayeayeayeaye["member_id"])
    message(f"Кажется, {getmention(randd.choice(hohlinki), 'dat')} не повезло.", disable_mentions=1)
else:
    message("Данная команда работает только в беседах!")