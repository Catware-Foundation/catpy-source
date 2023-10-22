# CatOS-Type Package
author = "aGrIk"
mode = "="
deps = 'None'
identificator = 'newyear'
command_ru = 'нг'
description = 'Считает, когда наступит новый год для города, указанного в команде. Если город не был указан в команде, рассчитывает для города в профиле.'

if parameter == "":
    if os.path.exists(f"users/{user_id}/city.txt"):
        geo = Geocode(ReadFF(f'users/{user_id}/city.txt'))
    else:
        userinfo = vk.users.get(user_ids=user_id, fields="city", lang=0)[0]
        if "city" in userinfo.keys():
            try:
                geo = Geocode(userinfo["city"]["title"])
            except:
                geo = Geocode("Москва")
        else:
            geo = Geocode("Москва")
else:
    try:
        geo = Geocode(parameter)
    except:
        geo = Geocode("Москва")

offset = cordstooffset(geo[0], geo[1])
nextyear = (datetime.datetime.now() + datetime.timedelta(seconds=offset)).year + 1
nextyear_unix = (datetime.datetime(nextyear, 1, 1) - datetime.timedelta(seconds=offset)).timestamp()

ret = "До нового " + str(nextyear) + " года в \"" + geo[2] + "\" осталось " + convertint(nextyear_unix - int(time.time())) + "!"

if parameter == "":
    ret += "\n\nЕсли ты хочешь посмотреть, когда наступит новый год в другом городе, напиши в конце команды этот город. Например: нг Киров"

message(ret, reply=True)
del geo
try:
    del userinfo
except:
    pass
