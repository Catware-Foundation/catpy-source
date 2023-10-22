# CatOS-type package
author = "catwared"
mode = "parameter"
deps = 'None'
identificator = 'enc'
command_ru = 'hex'
description = 'Кодировщик текста в HEX'

try:
    r = " ".join("{:02x}".format(ord(c)) for c in parameter)
    message(f"Результат: {r}", reply=True)
except Exception as e:
    message("Произошла ошибка при кодировании - " + str(e).upper().replace(" ", "_"), reply=True)
