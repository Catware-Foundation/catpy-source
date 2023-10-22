# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'spellchecker'
command_ru = 'орфография'
description = 'Проверяет текст на наличие орфографических ошибок на базе Яндекс.Спеллера'

ret = convertjson(Get("https://speller.yandex.net/services/spellservice.json/checkText?text=" + parameter.replace(" ", "+")))

if len(ret) == 0:
    message("Ошибок не обнаружено.", reply=True)
else:
    text_ret = parameter
    for cur in ret:
        text_ret = text_ret.replace(str(cur["word"]), str(cur["s"][0]))
    message("Исправленный вариант: " + text_ret, reply=True)
    del text_ret
del ret

