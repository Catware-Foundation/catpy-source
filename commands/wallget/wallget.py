# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'wallget'
command_ru = 'поиск'
description = 'Искать людей'

#hide

users = []
message("Поиск...")
try:
    users1 = vk2.users.search(q=parameter)
    for y in users1["items"]:
        users.append("[id" + str(y["id"]) + "|" + y["first_name"] + " " + y["last_name"] + "]")
    message("Найдены следующие пользователи:\n" + "\n".join(users), reply=True)
except Exception as e:
    message("Ошибка: " + str(e), reply=True)
del users
del users1

