# CatOS-Type Package
author = "aGrIk"
mode = "="
deps = 'None'
identificator = 'chance'
command_ru = 'шанс'
description = 'Прикидывает вероятность того или иного события'

arr = ["Шанс где-то около ", "Вероятно, в районе ", "Ставлю сотку, ", "Предполагаю, что ", "Как знать, но где-то ", "Справедливым будет назвать ", "Проверяй, "]

message(f"{randd.choice(arr)}{randd.randint(0, 100)}%", reply=True)