# CatOS-type package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'wikipos'
command_ru = 'место'
description = 'Поиск информации по геолокационной метке'

if "geo" in event.object.keys():
    latitude = str(event.object["geo"]["coordinates"]["latitude"])
    longitude = str(event.object["geo"]["coordinates"]["longitude"])

    ###СЛУЖЕБНОЕ
    #latitude = str(0.0)
    #longitude = str(0.0)
    #wikipedia.set_lang("ru")
    ###СЛУЖЕБНОЕ

    gay200 = wikipedia.geosearch(latitude, longitude, radius=200)
    gay500 = wikipedia.geosearch(latitude, longitude, radius=500)
    gay1000 = wikipedia.geosearch(latitude, longitude, radius=1000)
    gay2000 = wikipedia.geosearch(latitude, longitude, radius=2000)
    gay5000 = wikipedia.geosearch(latitude, longitude, radius=5000)
    gay10000 = wikipedia.geosearch(latitude, longitude, radius=10000)

    if len(gay200) == 10:
        text = "В радиусе 200 метров найдено:"
        for i in range(len(gay200)):
            text += "\n" + gay200[i] + " (" + ShortUrl(wikipedia.page(gay200[i]).url) + ")"
    elif len(gay500) == 10:
        text = "В радиусе 500 метров найдено:"
        for i in range(len(gay500)):
            text += "\n" + gay500[i] + " (" + ShortUrl(wikipedia.page(gay500[i]).url) + ")"
    elif len(gay1000) == 10:
        text = "В радиусе 1000 метров найдено:"
        for i in range(len(gay1000)):
            text += "\n" + gay1000[i] + " (" + ShortUrl(wikipedia.page(gay1000[i]).url) + ")"
    elif len(gay2000) == 10:
        text = "В радиусе 2000 метров найдено:"
        for i in range(len(gay2000)):
            text += "\n" + gay2000[i] + " (" + ShortUrl(wikipedia.page(gay2000[i]).url) + ")"
    elif len(gay5000) == 10:
        text = "В радиусе 5000 метров найдено:"
        for i in range(len(gay5000)):
            text += "\n" + gay5000[i] + " (" + ShortUrl(wikipedia.page(gay5000[i]).url) + ")"
    elif len(gay10000) > 0:
        text = "В радиусе 10000 метров найдено:"
        for i in range(len(gay10000)):
            text += "\n" + gay10000[i] + " (" + ShortUrl(wikipedia.page(gay10000[i]).url) + ")"
    else:
        text = "На 10 километров вокруг тишь да гладь. Википедия так сказала.☝🏻"
else:
    text = "Вы не прикрепили геометку."
message(text, reply=True)
