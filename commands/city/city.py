# CatOS-type package
author = 'aGrIk'
mode = '='
deps = 'None'
identificator = 'city'
command_ru = 'город'
description = 'Сохраняет/показывает населённый пункт по умолчанию для некоторых команд'

if parameter:
    try:
        city = Geocode(parameter)[2]
        writeTo(city, f"users/{user_id}/city.txt")
        message(f"Теперь \"{city}\" - ваш населённый пункт по умолчанию.\n\nВы имели ввиду другой населённый пункт? Повторите снова, уточнив запрос.")
    except:
        message("Нам не удалось найти такой населённый пункт. Уточните запрос и повторите снова.")
elif "geo" in event.object.keys():
    try:
        latitude = event.object["geo"]["coordinates"]["latitude"]
        longitude = event.object["geo"]["coordinates"]["longitude"]
        city = Geocode(f"{latitude}, {longitude}")[2]
        writeTo(f"{latitude}, {longitude}", f"users/{user_id}/city.txt")
        message(f"Теперь \"{city}\" - ваш населённый пункт по умолчанию.\n\nВы имели ввиду другой населённый пункт? Повторите снова, уточнив запрос.")
    except:
	    message("Нам не удалось найти населённый пункт. Уточните запрос и повторите снова.")
else:
    if os.path.exists(f"users/{user_id}/city.txt"):
        message(f"Ваш населённый пункт по умолчанию - {ReadFF(f'users/{user_id}/city.txt')}")
    else:
        message("Вы ещё не указывали населённый пункт. Самое время это сделать, введя \"/город\" и ваш населённый пункт.")
