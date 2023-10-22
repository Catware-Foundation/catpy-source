checking_id = ""
parameter = parameter.lower()
if parameter in commands:
    checking_id = ids[commands.index(parameter)]
elif parameter in os.listdir(COMMANDSDIR):
    checking_id = parameter

if checking_id:
    checking_json = convertjson(ReadFF(f"{COMMANDSDIR}/{checking_id}/{checking_id}.json"))
    ret = f'Название команды: {checking_json["command_ru"]}\nИдентификатор: {checking_json["identificator"]}\nАвторы: {checking_json["author"]}\nОписание: {checking_json["description"]}\n'
    if "tip" in checking_json.keys():
        ret += "Использование: " + checking_json["tip"] + "\n"
    if checking_json["testing"]:
        ret += f'\nТестируется: да\n'
    else:
        ret += f'Тестируется: нет\n'
    if checking_json["hide"]:
        ret += f'Скрыто: да\n'
    else:
        ret += f'Скрыто: нет\n'
    if checking_json["restricted"]:
        ret += f'Находится в дополнительном пакете: да\n'
    else:
        ret += f'Находится в дополнительном пакете: нет\n'
    if checking_json["disabled"]:
        ret += f'Отключена: да\n'
    else:
        ret += f'Отключена: нет\n'
    message(ret)
else:
    message("По вашему запросу не обнаружено ни одной команды. Проверьте правильность введённого параметра.")