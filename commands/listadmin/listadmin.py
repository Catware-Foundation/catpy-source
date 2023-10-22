# CatOS-Type Package
author = "aGrIk"
mode = "="
deps = 'None'
identificator = 'listadmin'
command_ru = 'списокадминов'
description = 'Выводит список администрации бота'

#hide

names = []

for e in admins.split(","):
    names.append(getmention(e))

message("Администрация бота:\n" + "\n".join(names), disable_mentions=1, reply=True)
