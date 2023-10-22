# CatOS-type package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'ship10'
command_ru = 'дшип'
description = 'Шипперство рандомных парочек в беседе - несколько штук за раз (по умолчанию 3, максимум 10)'
#disable
if event.from_chat:
    ships = []

    try:
        couples = int(parameter)
        if couples > 10 or couples < 1:
            couples = 3
    except:
        couples = 3

    love = 'любит,хочет,тайно возжелает,не представляет себя без,без ума от'.split(',')

    for x in range(couples):
        chatt = vk.messages.getConversationMembers(peer_id=peer_id)
        user1 = randd.choice(chatt["profiles"])["id"]
        user2 = randd.choice(chatt["profiles"])["id"]
        ships.append(getname(user1) + ' ' + randd.choice(love) + ' ' + getname(user2, "acc"))

    message("\n".join(ships), reply=True)
else:
    message("Это надо использовать в беседах. ", reply=True)
