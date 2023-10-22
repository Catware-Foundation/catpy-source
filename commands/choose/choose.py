# CatOS-type package
author = "aGrIk"
mode = "start"
deps = 'None'
identificator = 'choose'
command_ru = 'выбери'
description = 'Выбирает один элемент из нескольких перечисленных через "или" элементов'

arr = parameter.split(" или ")

choosers = "Кот выбрал,Древние оракулы выбрали,Сова выбрала, Разрабы котопая выбрали,Питон выбрал,Я выбрал,Рандом выбрал".split(",")

message(randd.choice(choosers) + " " + randd.choice(arr), reply=True)
