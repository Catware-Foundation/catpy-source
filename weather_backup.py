# CatOS-Type Package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'weather'
command_ru = 'погода'
description = 'Поиск прогноза погоды для населенного пункта.'

try:
    geo = Geocode(parameter)

    yura = convertjson(Get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(geo[0]) + "&lang=ru&lon=" + str(geo[1]) + "&appid=" + owm_token + "&units=metric"))

    #message("Сконвертировал этот высер")

    def get_wind_direction(deg):
        l = ['С','СВ','В','ЮВ','Ю','ЮЗ','З','СЗ']
        for i in range(0,8):
            step = 45.
            min = i*step - 45/2.
            max = i*step + 45/2.
            if i == 0 and deg > 360-45/2.:
                deg = deg - 360
            if deg >= min and deg <= max:
                res = l[i]
                break
        return res

    lat = yura["coord"]["lat"]
    lon = yura["coord"]["lon"]
    main = yura["weather"][0]["id"]
    desc = yura["weather"][0]["description"]
    temp = yura["main"]["temp"]
    feels = yura["main"]["feels_like"]
    temp_min = yura["main"]["temp_min"]
    temp_max = yura["main"]["temp_max"]
    city = yura["name"]
    cntr = yura["sys"]["country"]
    pressure = yura["main"]["pressure"]
    humidity = yura["main"]["humidity"]
    visibility = yura["visibility"]
    wind_speed = yura["wind"]["speed"]
    wind_deg = yura["wind"]["deg"]
    cloudness = yura["clouds"]["all"]

    #message("все ок, раскидал по переменным")

    cases = {
        200: "⛈",
        201: "⛈",
        202: "⛈",
        210: "⛈",
        211: "⛈",
        212: "⛈",
        221: "⛈",
        230: "⛈",
        231: "⛈",
        232: "⛈",
        300: "🌧",
        301: "🌧",
        302: "🌧",
        310: "🌧",
        311: "🌧",
        312: "🌧",
        313: "🌧",
        314: "🌧",
        321: "🌧",
        500: "🌧",
        501: "🌧",
        502: "🌧",
        503: "🌧",
        504: "🌧",
        511: "❄",
        520: "🌧",
        521: "🌧",
        522: "🌧",
        531: "🌧",
        600: "❄",
        601: "❄",
        602: "❄",
        611: "❄",
        612: "❄",
        613: "❄",
        615: "❄",
        616: "❄",
        620: "❄",
        621: "❄",
        622: "❄",
        701: "🌫️",
        711: "🌫️",
        721: "🌫️",
        731: "🌫️",
        741: "🌫️",
        751: "🌫️",
        761: "🌫️",
        762: "🌫️",
        771: "🌫️",
        781: "🌫️",
        800: "☀️",
        801: "☁",
        802: "☁",
        803: "☁",
        804: "☁",
    }
    result = cases.get(main, None)

    #message("кейсы готовы, результат " + result)

    #message("Все в порядке его появления: " + cntr + " " + city + " " + lat + " " + lon + " " + result + " " + desc.capitalize() + " " + temp + " " + feels + " " + temp_min + " " + temp_max)

    message("По информации OpenWeatherMap, в локации " + cntr + ", " + city + " (" + str(lat) + ", " + str(lon) + """) сейчас:
    """ + result + " " + desc.capitalize() + ", " + str(temp) + "°C (ощущается как " + str(feels) + "°C), варьирования " + str(temp_min) + ".." + str(temp_max) + """°C
    💨 Ветер: """ + str(wind_speed) + " м/с, метеорологическое направление " + str(wind_deg) + "° (" + str(get_wind_direction(int(wind_deg))) + """)
    💧 Влажность воздуха: """ + str(humidity) + """%
    👀 Видимость: """ + str(visibility) + """ метров
    ☁ Облачность: """ + str(cloudness) + """%
    🌎 Давление: """ + str(round(pressure / 1.333)) + """ мм. рт. ст.

    """)

except:
    message("""По вашему запросу ничего не было найдено.

    Проверьте, корректно ли указано место. Если все верно - отправьте его нам командой репорт.""")