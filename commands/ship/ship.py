# CatOS-type package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'ship'
command_ru = 'шип'
description = 'Шипперство рандомных парочек в беседе'

if event.from_chat:
    love = 'любит,хочет,тайно возжелает,не представляет себя без,без ума от'.split(',')
    chatt = vk.messages.getConversationMembers(peer_id=peer_id)
    user1 = randd.choice(chatt["profiles"])["id"]
    user2 = randd.choice(chatt["profiles"])["id"]
    message(getmention(user1) + ' ' + randd.choice(love) + ' ' + getmention(user2, "acc"), reply=True)
    del love
    del chatt
    del user1
    del user2
else:
    message("Это надо использовать в беседах. ", reply=True)
