# CatOS-type package
author = "catwared"
mode = "="
deps = 'None'
identificator = 'usersurr'
command_ru = 'стат'
description = 'Некоторая интересная статистика.'

message(f"""Статистика:
Использовано команд (вами) -> {getparam(user_id, "score")}""", reply=True)
