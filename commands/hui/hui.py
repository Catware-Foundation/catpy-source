# CatOS-type package
author = 'а кто'
mode = '='
deps = 'None'
identificator = 'hui'
command_ru = 'хуй'
description = 'а где'
#hide
ret = randd.choice(["Х", "х"]) + randd.choice(["У", "у"]) + randd.choice(["Й", "й"])

for ayeayayayayayayaeeeeeee in range(randd.randint(5, 20)):
    ret += randd.choice([")", "(", ")", "(", "0", "9"])

if randd.randint(0, 100) == 28: ret = "ебать пасхалка! плюс один миска рис"

message(ret, reply=False)
