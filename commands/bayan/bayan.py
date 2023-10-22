# CatOS-Type Package
author = "aGrIk"
mode = "="
deps = 'None'
identificator = 'bayan'
command_ru = 'баян'
description = "Показывает случайный анекдот (спойлер: баян)"

num = randd.choice("1,11".split(","))
lol = randd.choice("Ха!!!!!! Ржу!!!!!!!!!!!!;На анекдот;Ахахах ржали всем кетвейром;СМИШНЯФКА!!! ХА!!!;Лови анекдот;Анекдот (ржать);УМОРА!!!)))))))))))));Ахаха смешно!!!!🤣🤣🤣🤣👍🏻👍🏻👍🏻;ОР!!!))))))))) АХХАХАХАХА!!!!!!!!!!!!!!!))))))".split(";"))

message(lol + ":\n" + requests.get("http://rzhunemogu.ru/RandJSON.aspx?CType=" + num).text.replace('{"content":"', '').replace('"}', ''), reply=True)

#restricted