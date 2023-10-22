# CatOS-Type Package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'weather'
command_ru = 'погода'
description = 'Поиск прогноза погоды для населенного пункта.'

weather_tm = time.time()
e_exists = False

try:
    if parameter == "":
        if "geo" in event.object.keys():
            latitude = event.object["geo"]["coordinates"]["latitude"]
            longitude = event.object["geo"]["coordinates"]["longitude"]
            geo = Geocode(f"{latitude}, {longitude}")
        elif os.path.exists(f"users/{user_id}/city.txt"):
            geo = Geocode(ReadFF(f'users/{user_id}/city.txt'))
        else:
            userinfo = vk.users.get(user_ids=user_id, fields="city", lang=0)[0]
            if "city" in userinfo.keys():
                geo = Geocode(userinfo["city"]["title"])
            else:
                raise Exception("Ахахах город не указан")
    else:
        geo = Geocode(parameter)

    yura = convertjson(Get(f"https://api.openweathermap.org/data/2.5/weather?lat={geo[0]}&lang=ru&lon={geo[1]}&appid={owm_token}&units=metric"))
    ivan = convertjson(Get(f"https://api.openweathermap.org/data/2.5/forecast?lat={geo[0]}&lang=ru&lon={geo[1]}&units=metric&appid={owm_token}"))
    suninfo = ssorg(geo[0], geo[1])


    def gwd(deg):
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

    #Current weather variables
    lat = yura["coord"]["lat"]
    lon = yura["coord"]["lon"]
    main = yura["weather"][0]["id"]
    desc = yura["weather"][0]["description"]
    temp = round(yura["main"]["temp"], 1)
    feels = round(yura["main"]["feels_like"], 1)
    temp_min = round(yura["main"]["temp_min"], 1)
    temp_max = round(yura["main"]["temp_max"], 1)
    pressure = yura["main"]["pressure"]
    humidity = yura["main"]["humidity"]
    visibility = yura["visibility"]
    wind_speed = yura["wind"]["speed"]
    wind_deg = yura["wind"]["deg"]
    cloudness = yura["clouds"]["all"]

    forecast = ivan["list"][:10]
    timezone = suninfo[10]
    sunrise = suninfo[0]
    sunset = suninfo[1]
    currtime = time.time() + timezone


    def emoji(id):
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
            804: "☁"
        }
        return cases.get(id, None)

    def moon():
        mn = astr_moon.phase(datetime.datetime.fromtimestamp(currtime).date())
        if mn < 3.5:
            return "🌑 Новолуние"
        elif mn < 7:
            return "🌒 Молодая луна"
        elif mn < 10.5:
            return "🌓 Первая четверть"
        elif mn < 14:
            return "🌔 Прибывающая луна"
        elif mn < 17.5:
            return "🌕 Полнолуние"
        elif mn < 21:
            return "🌖 Убывающая луна"
        elif mn < 24.5:
            return "🌗 Последняя четверть"
        elif mn < 28:
            return "🌘 Старая луна"


    sunstate = ""
    if (currtime > sunrise) and (currtime < sunset):
        sunstate = "☀ Световой день"
        dex = deunix(sunset)
        sunstate += f", темнеть начнёт в {dex[3]}:{dex[4]}:{dex[5]}"
    elif (suninfo[4] <= currtime) and (currtime <= sunrise):
        sunstate = "🌅 Рассвет"
        dex = deunix(sunrise)
        sunstate += f", полностью рассветёт в {dex[3]}:{dex[4]}:{dex[5]}"
    elif (sunset <= currtime) and (currtime <= suninfo[5]):
        sunstate = "🌇 Сумерки"
        dex = deunix(suninfo[5])
        sunstate += f", полностью стемнеет в {dex[3]}:{dex[4]}:{dex[5]}"
    else:
        sunstate = "🌃 Ночь"
        tomorrow_sr = ssorg(geo[0], geo[1], (datetime.datetime.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))[4]
        if currtime < suninfo[4]:
            dex = deunix(suninfo[4])
        else:
            dex = deunix(tomorrow_sr)
        sunstate += f", светать начнёт в {dex[3]}:{dex[4]}:{dex[5]}"

    weather_res = f"""
Локация "{geo[2]}" ({lat}, {lon}):
{emoji(main)} {desc.capitalize()}, {temp}°C (ощущается как {feels}°C), варьирования {temp_min}..{temp_max}°C
💨 Ветер: {wind_speed} м/с, {wind_deg}° ({gwd(int(wind_deg))})
💧 Влажность воздуха: {humidity}%
👀 Видимость: {visibility} метров
☁ Облачность: {cloudness}%
🌎 Давление: {round(pressure / 1.333)} мм. рт. ст.

☀ Солнце: {sunstate}
🌅 Восход: {deunix(sunrise)[3]}:{deunix(sunrise)[4]}:{deunix(sunrise)[5]}
🌇 Закат: {deunix(sunset)[3]}:{deunix(sunset)[4]}:{deunix(sunset)[5]}
☀ Полдень: {deunix(suninfo[2])[3]}:{deunix(suninfo[2])[4]}:{deunix(suninfo[2])[5]}
🌝 Световой день: {convertint(suninfo[3])}

{moon()}

Погода по часам:
    """

    for count in forecast:
        weather_res += f'{emoji(count["weather"][0]["id"])} {readableDate(count["dt"] + timezone, False, False)} - {count["weather"][0]["description"].capitalize()}: {round(count["main"]["temp"], 1)}°C, {round(count["wind"]["speed"], 1)} м/с, {count["wind"]["deg"]}° ({gwd(count["wind"]["deg"])})\n'

    weather_res += "\n Информация взята с ресурса OpenWeatherMap."
except Exception as e:
    weather_res = """По вашему запросу ничего не было найдено.

    Проверьте, корректно ли указано место, либо есть ли у вас в профиле какой-либо населённый пункт."""
    e_exists = True
    global exc
    exc = str(e)
if user_id == 242722587:
    weather_res += f"\n\nОтладочная информация: \nВремя ответа: {time.time() - weather_tm}\nПараметр: \"{parameter}\""
    if e_exists: weather_res += f"Exception: {exc}\n"

message(weather_res, reply=True)
