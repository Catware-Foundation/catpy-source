# CatOS-type package
author = 'aGrIk'
mode = '='
deps = 'None'
identificator = 'tester'
command_ru = 'тестер'
description = 'Показывает информацию о тестировщике (текущий пользователь по умолчанию)'
#hide
#testing
if parameter == "":
    uid = user_id
else:
    try:
        uid = getid(parameter)
        if uid == None:
            uid = testerinfo(user_id)
    except:
        uid = testerinfo(user_id)

if testpathexists(uid):
    if parameter == "":
        tstjson = testerinfo(uid)
    else:
        try:
            tstjson = testerinfo(uid)
        except:
            tstjson = testerinfo(uid)

    if not tstjson["tester"]:
        additional = "Не является тестировщиком с "
    else:
        additional = "Тестировщик с "

    message(f'''Информация о тестировщике {getmention(tstjson["id"], "abl")}:
ID: {tstjson["id"]}
Статус: {tstjson["status"]}
В программе: {str(tstjson["tester"]).replace("True", "да").replace("False", "нет")}
Успешных репортов: {tstjson["reports"]}

Дата регистрации в программе: {readableDate(tstjson["first_invite"])} UTC+0 ({convertint(time.time() - tstjson["first_invite"])} назад)
{additional} {readableDate(tstjson["last_invite"])} UTC+0 ({convertint(time.time() - tstjson["last_invite"])} назад)''')
else:
    message("Пользователь не является тестировщиком.")
