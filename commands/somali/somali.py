# CatOS-Type Package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'somali'
command_ru = 'кек'
description = 'Разговаривать с идиотом'

result = translator.translate(parameter, lang_tgt = 'so')
ar = result
result = translator.translate(ar, lang_tgt = 'ru')
message(result, reply=True)
