# CatOS-Type Package
author = "Cat Weird"
mode = "="
deps = 'None'
identificator = 'advice'
command_ru = 'совет'
description = 'Охуенный блять совет (взято с сайта fucking-great-advice.ru)'

#restricted

jsonn = convertjson(Get("http://fucking-great-advice.ru/api/random"))
message(f"Охуенный блять совет: {convertjson(Get('http://fucking-great-advice.ru/api/random'))['text']}", reply=True)
