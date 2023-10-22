# CatOS-Type Package
author = "aGrIk"
mode = "start"
deps = 'None'
identificator = 'whois'
command_ru = 'вычислить'
description = 'Вытягивает всю инфу про айпи из WHOIS.\nИспользование: /вычислить имяхоста'
try:
    json1337 = convertjson(Get("http://api.whois.vu/?s=ip&q=" + parameter + "&clean"))
    message("Информация по " + json1337['hostname'] + " (" + json1337['ip'] + ") от WHOIS:\n\n" + json1337['whois'], reply=True)
    del json1337
except:
    message("Введено некорректное имя хоста. Или нет?", reply=True)

