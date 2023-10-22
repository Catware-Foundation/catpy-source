# CatOS-Type Package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'bread'
command_ru = 'бред'
description = 'Генерация рандомного бреда на основе различных текстов'

try:
    message(Get("https://catwareai.ctw.re/bread"), reply=True)
except:
    message("Не знаю.", reply=True)
