# CatOS-Type Package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'response'
command_ru = 'ответить'
description = 'Ответ на репорт [только для администраторов]'

#hide

if str(user_id) in admins:
    message('Отправка сообщения...')
    surr_text = event.object['reply_message']['text']
    user_idby = int(surr_text[int(surr_text.index("["))+1:int(surr_text.index("|"))].replace("id", ''))
    message_ts = parameter
    try:
        messagecust('Вам сообщение от [id' + str(user_id) + '|администратора]:\n' + message_ts, user_idby, intent="customer_support")
        mta(f"Администратор {getmention(user_id)} ({user_id}) ответил на репорт {getmention(user_idby)} ({user_idby}):\n{message_ts}")
    except Exception as e:
        message('Не удалось отправить сообщение: ' + str(e), reply=True)
    del surr_text
    del user_idby
    del message_ts
else:
    message("Вы не обнаружены в списке администраторов!", reply=True)

#hide
