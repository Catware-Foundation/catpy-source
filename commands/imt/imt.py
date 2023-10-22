# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'imt'
command_ru = 'имт'
description = 'Рассчитывает ваш индекс массы тела. Использование: /имт [рост в см] [вес в кг]'
#testing
doin = True
param = parameter.split(" ")
try:
    for aye in range(len(param)):
        param[aye] = int(param[aye])
    if param[0] <= 0 or param[1] <= 0 or len(param) != 2: doin = False
    imt = round(param[1] / ((param[0] / 100) ** 2), 2)
    if 0 < imt < 16:
        add = "выраженный дефицит массы тела"
    elif 16 <= imt < 18.5:
        add = "недостаточная масса тела"
    elif 18.5 <= imt < 25:
        add = "норма"
    elif 25 <= imt < 30:
        add = "избыточная масса тела, предожирение"
    elif 30 <= imt < 35:
        add = "ожирение 1 степени"
    elif 35 <= imt < 40:
        add = "ожирение 2 степени"
    elif 40 <= imt < 45:
        add = "ожирение 3 степени"
    elif imt >= 45:
        add = "ожирение 4 степени"
except:
    doin = False

if doin:
    message(f"Ваш индекс массы тела: {imt} ({add})")
else:
    message("Некорректно введены параметры. Использование: /имт [рост в см] [вес в кг]")
