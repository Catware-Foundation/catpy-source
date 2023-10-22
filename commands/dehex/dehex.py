# CatOS-type package
author = "catwared, https://vk.com/voroninmine"
mode = "parameter"
deps = 'None'
identificator = 'dehex'
command_ru = 'dehex'
description = 'Декодировщик текста из HEX'

try:
    r = ''.join(map(lambda i: chr(int(i, base=16)), parameter.split()))
    message(f"Результат: {r}", reply=True)
except Exception as e:
    message("Произошла ошибка при декодировании - " + str(e).upper().replace(" ", "_"), reply=True)
