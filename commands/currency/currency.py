# CatOS-type package
author = 'aGrIk, platofff'
mode = '='
deps = 'None'
identificator = 'currency'
command_ru = 'курс'
description = 'Выводит курс валют по данным ЦБ РФ'

currency = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
currencydate = currency["Date"].split("T")[0].split("-")
currency_ret = f"""Курс валют на {currencydate[2]}.{currencydate[1]}.{currencydate[0]} по данным Центробанка РФ:\n"""
btc = convertjson(Get("https://blockchain.info/ticker"))

for now_curr in currency["Valute"].keys():
    nc = currency["Valute"][now_curr]
    currency_ret += f"{nc['Nominal']} {nc['Name']} - {nc['Value']} рублей "
    vari = round(nc["Value"] - nc["Previous"], 4)
    if vari < 0:
        currency_ret += f"({vari})"
    else:
        currency_ret += f"(+{vari})"
    currency_ret += "\n"

currency_ret += f"\nКриптовалюты:\nBitcoin - ${btc['USD']['last']} ({btc['RUB']['last']}₽)"
message(currency_ret, reply=True)
