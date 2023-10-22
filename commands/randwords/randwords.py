# CatOS-type package
author = "catwared, Илья Бурдахин"
mode = "start"
deps = 'None'
identificator = 'randwords'
command_ru = 'ёда'
description = 'Перемешка слов'

s_ = parameter.split(" ")
randd.shuffle(s_)
message("Результат: " + " ".join(s_), reply=True)
