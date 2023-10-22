# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'olban'
command_ru = 'олбан'
description = 'Олбанизатор, коверкойущий всйо в олбанскей'

res = parameter.lower()
if "ё" in res:
    res = res.replace("ё", "йо")
elif "йо" in res:
    res = res.replace("йо", "ё")
res = res.replace("ю", "йу")
if "в" in res:
    res = res.replace("в", "фф")
if "ае" in res:
    res = res.replace("ае", "ои")
if "ться" in res or "тся" in res or "тьса" in res or "тса" in res:
    res = res.replace("ться", "ца").replace("тся", "ца")

message(res, reply=True)
