# CatOS-type package
author = "catwared"
mode = "parameter"
deps = 'None'
identificator = 'xitext'
command_ru = 'кси'
description = 'Команда который превращать ваш русский в ломать русский'

message(Get(f"https://catwareai.ctw.re/xitext?text={parameter}"))
