# CatOS-Type Package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'bread2'
command_ru = 'порф'
description = 'Генерация рандомного бреда на основе различных текстов'

try:
    message(Get("https://catwareai.ctw.re/porfd?text=" + parameter), reply=True)
except:
    message("Не знаю.", reply=True)
