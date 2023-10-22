# CatOS-Type Package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'yap'
command_ru = 'перевод'
description = 'Перевод текста с помощью Google Translate\nИспользование команды: перевод -<рус/анг/нем> <текст>'

if "-рус" in flags:
    result = translator.translate(parameter, lang_tgt = 'ru')
    message(result, reply=True)

elif "-анг" in flags:
    result = translator.translate(parameter, lang_tgt = 'en')
    message(result, reply=True)

elif "-нем" in flags:
    result = translator.translate(parameter, lang_tgt = 'de')
    message(result, reply=True)
