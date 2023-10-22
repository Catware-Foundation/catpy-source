# CatOS-type package
author = 'aGrIk'
mode = '='
deps = 'None'
identificator = 'chat'
command_ru = 'чат'
description = 'Функционал для админов бесед'

executing = True
try:
    chat_admins = chatadmins(peer_id)
except:
    chat_admins = []
    executing = False

if (user_id in chat_admins or (str(user_id) in admins and "-su" in flags)) and user_id != peer_id and executing:
    parameter = parameter.replace(" -su", "").replace("-su", "")
    if parameter == "":
        message(
"""
Утилиты для администраторов бесед:

Кик:
Выгоняет участника из беседы
Вы можете переслать сообщение исключаемого участника или указать ссылку на него.
Пример: /чат кик durov

Алерт:
Включает/отключает уведомления об участниках
Пример: /чат алерт

Антиспам:
Включает/отключает отправку длинных сообщений в лс, а не в чат
Пример: /чат антиспам

Правила:
Устанавливает текст правил для пришедших в беседу.
Просмотреть текст правил можно командой \"правила\".
Пример: /чат правила Беседа без правил!

Закреп:
Закрепляет приложенное сообщение
Пример: /чат закреп

Откреп:
Открепляет закреплённое в данный момент сообщение
Пример: /чат откреп

Название:
Меняет название чата
Пример: /чат название Беседа класса""", reply=True)
    else:
        _command = parameter.split(" ")[0]
        _param = " ".join(parameter.split(" ")[1:])

        if _command == "кик":
            try:
                kicking = True
                if _param:
                    _user = getid(_param)
                elif 'reply_message' in event.object.keys():
                    _user = event.object['reply_message']['from_id']
                elif event.object['fwd_messages']:
                    _user = event.object['fwd_messages'][0]['from_id']
                else:
                    message("Вы не указали, кого кикать.")
                    kicking = False

                if kicking: 
                    vk.messages.removeChatUser(member_id=_user, random_id=rid(), chat_id=peer_id - 2000000000)
                    message(f"{getmention(_user)} был успешно исключён из чата! Вы можете пригласить его обратно.", reply=True)
            except vk_api.exceptions.ApiError as e:
                if str(e) == "[113] Invalid user id":
                    message("Мне не удалось кикнуть этого пользователя, поскольку его не существует.", reply=True)
                elif str(e) == "[935] User not found in chat":
                    message("Мне не удалось кикнуть этого пользователя, поскольку он не состоит в этом чате.", reply=True)
                else:
                    message("Мне не удалось кикнуть этого пользователя.", reply=True)

        if _command == "алерт":
            peer_id = str(peer_id)
            if peer_id not in alrts:
                PlusWrite(f"{peer_id}\n", "chats/alerts.txt")
                message("Теперь в данную беседу будут отправляться уведомления о вошедших/вышедших участниках.", reply=True)
            else:
                writeTo(alrts.replace(f"{peer_id}\n", ""), "chats/alerts.txt")
                message("Теперь в данную беседу не будут отправляться уведомления о вошедших/вышедших участниках.", reply=True)

        if _command == "антиспам":
            if str(peer_id) not in ReadFF("chats/antispam.txt"):
                PlusWrite(f"{peer_id}\n", "chats/antispam.txt")
                message("Теперь сообщения длиннее 2000 символов будут отправляться в личные сообщения!", reply=True)
            else:
                writeTo(ReadFF("chats/antispam.txt").replace(f"{peer_id}\n", ""), "chats/antispam.txt")
                message("Анти-спам политика отключена: теперь все сообщения будут отправляться в беседу.", reply=True)

        if _command == "правила" and _param:
            try:
                writeTo(_param, "chats/" + str(chat_id) + "/rules.txt")
                message("Правила успешно установлены", reply=True)
            except:
                message("Произошла неизвестная ошибка.", reply=True)

        if _command == "откреп":
            vk.messages.unpin(peer_id=peer_id)
            message("Сообщение откреплено.", reply=True)
            
        if _command == "закреп":
            if 'reply_message' in event.object.keys():
                vk.messages.pin(peer_id=peer_id, message_id=vk.messages.getByConversationMessageId(peer_id=peer_id, conversation_message_ids=event.object["reply_message"]["conversation_message_id"])["items"][0]["id"])
                message("Сообщение закреплено!", reply=True)
            else:
                message("Приложите закрепляемое сообщение.", reply=True)
                
        if _command == "название" and _param:
            try:
                #if peer_id != 2000000072:
                vk.messages.editChat(chat_id=event.chat_id, title=_param)
                message("Успешно!", reply=True)
            except:
                message("Смена названия не удалась.", reply=True)
            
            
elif "-ali" in parameter and user_id == 664735292:
    message("али)")
elif user_id == peer_id:
    message("Управление чатами может осуществляться только в самих чатах!", reply=True)
elif not executing:
    message("Кажется, я не являюсь администратором этого чата! Назначьте меня админом и попробуйте снова.", reply=True)
elif "-y" in parameter and user_id == getid("polybar"):
    message("Йогурт, ты дурак!", reply=True)
else:
    message("Вы не являетесь админом этого чата!", reply=True)


