# CatOS-Type Package
author = "catweird"
mode = "start"
deps = 'None'
identificator = 'cici'
command_ru = 'дуракшифр'
description = 'Такой себе шифр (команды дешифр/шифр)'

#disable
exec(ReadFF("lib/cipher-eban.py"))

cmds = parameter.split(" ")
eban = " ".join(cmds[1:])

if cmds[0] == "дешифр":
    try:
        message(decode(eban), reply=True)
    except:
        message("Неверный шифр", reply=True)

if cmds[0] == "шифр":
    message(encode(eban))

if cmds[0] not in "шифр дешифр":
    message("Неверно введена команда", reply=True)
