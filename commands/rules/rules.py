# CatOS-type package
author = "catwared"
mode = "="
deps = 'None'
identificator = 'rules'
command_ru = 'правила'
description = 'Правила для определённой беседы.'
#hide

if event.from_chat:
    message(ReadFF("chats/" + str(chat_id) + "/rules.txt"), reply=True)
else:
    message("Данная команда предназначена только для чатов.", reply=True)
