# CatOS-type package
author = 'Cat Weird'
mode = '='
deps = 'None'
identificator = 'gun'
command_ru = 'ган'
description = 'Выдаёт всратое оружие'
#hide

callibres = "7.62х39/7.62х51/7.62х25/5.56х39/5.45х39/50бмг/9х19/45апс".split("/")
names = "Калашникова,Драгунова,Макарова,Шпагина,Стечкина,Лебедева".split(",")
types = "Пистолет,Автомат,Пулемёт,Пистолет-пулемёт,Арбалет,Снайперская винтовка,Штурмовая винтовка,Дробовик".split(',')

message(f"Оружие: {randd.choice(types)} {randd.choice(names)}\n\nКалибр: {randd.choice(callibres)}")
