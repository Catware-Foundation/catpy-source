# CatOS-type package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'enshort'
command_ru = 'enshort'
description = 'Сократитель английских слов и названий. К примеру, catware -> ctwr'

message("Результат: " + parameter.replace("e", "").replace("y", "").replace("i", "").replace("o", "").replace("a", ""), reply=True)
