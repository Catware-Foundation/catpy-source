# CatOS-Type Package
author = "catwared"
mode = "="
deps = 'None'
identificator = 'enable'
command_ru = 'подключить-пакет'
description = 'Подключить пакет потенциально оскорбительных команд.'

if str(user_id) not in ReadFF("usr/restricted.txt").split(","):
    listd = ReadFF("usr/restricted.txt").split(",")
    listd.append(str(user_id))
    writeTo(",".join(listd), "usr/restricted.txt")
    message("Подключён пакет команд, которые были отмечены нами как потенциально оскорбительные и не предназначенные для просмотра на работе. Catware не несёт ответственности за последствия использования данных команд. Их список можно просмотреть при помощи \"/команды -доп\". Отключить пакет можно, введя команду повторно.", reply=True)

else:
    listd = ReadFF("usr/restricted.txt").split(",")
    listd.remove(str(user_id))
    writeTo(",".join(listd), "usr/restricted.txt")
    message("Пакет успешно отключен, введи команду ещё раз, если хочешь вернуть.", reply=True)
