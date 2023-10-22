# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'cipher2'
command_ru = 'дешифр'
description = 'Дешифровка Котошифра'

exec(ReadFF("lib/catcipher.py"))

message("Результат: " + decipher(parameter), reply=True)
