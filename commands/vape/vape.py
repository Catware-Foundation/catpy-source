# CatOS-type package
author = 'Cat Weird'
mode = '='
deps = 'None'
identificator = 'vape'
command_ru = 'девайс'
description = 'Советует лютый вейп девайс'

#hide

devices = "Knight,Pasito,Minifit,Drag,Aegis,Vaporesso,Santi,Battlestar,Charon,Catpy,Huawei,Intel,Aye,iJust,Pico,JUUL,SMOK".split(",")
editions = "80,2,Max,Nano,X,Boost,Boost Plus,Hero,Barr,Osmall,Xros,,Baby,(говно),(не советую),3,S,RPM 2,MagicPod,Nova 2".split(",")
types = "Бокс-мод,Под,Вейп,Под-мод,Мехмод".split(",")
mf = "Smoant,Voopoo,Justfog,Dentsu,Vaporesso,позалупа".split(",")
measurings = ["мл", "литров", "кг", "метров"]

message(f"Советую купить: {randd.choice(types)} {randd.choice(devices)} {randd.choice(editions)}\n\nЦена: {str(randd.randint(0, 5000))} руб.\nМощность: {str(randd.randint(7, 400))} {randd.choice(['лошадиных сил','Вт'])}.\nКартридж: {str(randd.randint(1, 9))} {randd.choice(measurings)}\nСопротивление: 0.{str(randd.randint(1, 8))} Ω\nПроизводитель: {randd.choice(mf)}")
