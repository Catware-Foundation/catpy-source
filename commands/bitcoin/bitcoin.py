# CatOS-type package
author = 'platofff, aGrIk'
mode = '='
deps = 'None'
identificator = 'bitcoin'
command_ru = 'биткоин'
description = 'Текущий курс биткоина'

btc = convertjson(Get("https://blockchain.info/ticker"))

if user_id == 230627315:
    message(f"${btc['USD']['last']} {btc['RUB']['last']}₽\nбля нирок че на завтра задали")
else:
    message(f"BTC сейчас стоит ${btc['USD']['last']} или {btc['RUB']['last']}₽")

