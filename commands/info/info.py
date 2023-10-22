# CatOS-Type Package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'info'
command_ru = 'инфо'
description = 'Информация о боте и разработчиках'

if only_admins:
    addition = "(безопасный режим)"
else:
    addition = ""

message(f'''Catware CatPy {version} Stable (от {releasedate})
Codename: {codename}
Работает под управлением {abms_name} {addition}
Интерпретатор: Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} {sys.version_info.releaselevel.capitalize()} на ОС {osname}

Система:

Кол-во пакетов: {str(len(commands))}
Кол-во сервисов: {str(len(os.listdir('services')))}
Кол-во CatLib'ов: {str(len(os.listdir('lib')))}
Примерное кол-во пользователей: {str(len(os.listdir('users')))}
Примерное кол-во бесед: {str(len(os.listdir('chats')))}

Информация о разработчиках:
Разработчики - @catweird и @theagrik
Домашняя страница - ctw.re
Catware Wiki - wiki.ctw.re''', disable_mentions=1, reply=True)
