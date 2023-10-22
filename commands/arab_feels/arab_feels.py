# CatOS-Type Package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'arab_feels'
command_ru = 'араб'
description = 'разговаривать с арабом'

if "-мега" not in parameter:
    result = translator.translate(parameter, lang_tgt='zh-tw')
    ar = Reverse(result)
    result = translator.translate(ar, lang_tgt='ru')
    message(result, reply=True)
else:
    negr = True
    buffersize = 0
    result = parameter.replace("-мега", "")
    message("Вычисление мегаарабской коронной фразы: выполняется 100 прогонов....")
    while buffersize < 100:
        buffersize += 1 
        result = translator.translate(result, lang_tgt="zh-tw")
        ar = Reverse(result)
        result = translator.translate(ar, lang_tgt="ru")
    message(result, reply=True)
