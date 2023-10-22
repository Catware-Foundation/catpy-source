# CatOS-type package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'rephrase'
command_ru = 'перефраз'
description = 'Перефразирование текста с помощью Google Переводчика'

aye = translator.translate(parameter, lang_tgt = 'ru')
aye = translator.translate(aye, lang_tgt = 'en')
res = translator.translate(aye, lang_tgt = 'ru')
message(res, reply=True)
