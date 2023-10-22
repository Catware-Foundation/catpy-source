# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'cipher'
command_ru = 'шифр'
description = 'Шифрование в Котошифр'

exec(ReadFF("lib/catcipher.py"))

message(cipher(parameter), reply=True)
