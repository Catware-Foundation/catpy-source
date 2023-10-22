alrts = ReadFF("chats/alerts.txt")
if "action" in event.object.keys():
    action = event.object["action"]["type"]
    tip = "\n\n"
    if ReadFF("chats/" + str(event.chat_id) + "/rules.txt") != "Правила не установлены.":
        tip += "В беседе есть правила! Ознакомься с ними по команде <</правила>>."

    if str(peer_id) in alrts or peer_id == 2000000072:
        greetings = "catpy приветствует тебя, ;Добро пожаловать к нам, ;Приветствуем тебя, о ".split(";")

        if action == "chat_invite_user":
            message(getmention(user_id) + " приглашает в беседу " + getmention(event.object["action"]["member_id"], "acc"))
            message(randd.choice(greetings) + getmention(event.object["action"]["member_id"]) + "! Я catpy, пожалуй, самый полезный чат-бот ВКонтакте :)\n\nПодробное описание моих команд: https://catware.space/commands.html \nАктуальный список команд: команды -лист\nДополнительный пакет команд: команды -доп\n\nПользоваться мною довольно просто: перед командой в беседе нужно написать \"/\" или \"кот \"!{}".format(tip), 0)

        elif action == "chat_invite_user" and event.object["action"]["member_id"] == gid:
           pass
        elif action == "chat_kick_user":
            if user_id != event.object["action"]["member_id"]:
                #pass
                message(getmention(user_id) + " выгоняет из беседы " + getmention(event.object["action"]["member_id"], "acc"))
            else:
                message(getmention(user_id) + " покидает эту беседу.")
            if event.object["action"]["member_id"] == getid("animeoftop"): message("Пизда копчёному))")


        elif action == "chat_invite_user_by_link":
            message(getmention(user_id) + " присоединяется к беседе по ссылке")
            message(randd.choice(greetings) + getmention(event.object["action"]["member_id"]) + "! Я catpy, пожалуй, самый полезный чат-бот ВКонтакте :)\n\nПодробное описание моих команд: https://catware.space/commands.html \nАктуальный список команд: команды -лист\nДополнительный пакет команд: команды -доп\n\nПользоваться мною довольно просто: перед командой в беседе нужно написать \"/\" или \"кот \"!{}".format(tip), 0)

    #
    # Кастомные условия
    #
    else:
        procmsg(f"В беседе произошло действие {action}, оно не будет обработано.\n")

    if action == "chat_title_update" and peer_id == 2000000072:
        vk.messages.editChat(chat_id=72, title="Филиал разработки ПО имени Кетвейра Котопаевского")
        messagecust("[action-handler] А-а, а вот хуй тебе", 2000000072)
