# CatOS-type package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'translit'
command_ru = 'транслит'
description = 'Транслитерация текста на русском языке'

exec(ReadFF("lib/transliterate.py"))
message(transliterate(parameter))
