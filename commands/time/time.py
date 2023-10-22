# CatOS-Type Package
author = "aGrIk"
mode = "="
deps = 'None'
identificator = 'time'
command_ru = 'время'
description = "Показывает время"

if parameter == "":
    if os.path.exists(f"users/{user_id}/city.txt"):
        geo = Geocode(ReadFF(f'users/{user_id}/city.txt'))
    else:
        userinfo = vk.users.get(user_ids=user_id, fields="city", lang=0)[0]
        if "city" in userinfo.keys():
            try:
                geo = Geocode(userinfo["city"]["title"])
            except:
                geo = Geocode("Гринвич")
        else:
            geo = Geocode("Гринвич")
else:
    try:
        geo = Geocode(parameter)
    except:
        geo = Geocode("Гринвич")

offset = cordstooffset(geo[0], geo[1])

utcdt = datetime.datetime.fromtimestamp(vk.utils.getServerTime())
dt = datetime.datetime.fromtimestamp(vk.utils.getServerTime() + offset)

if offset < 0:
    strtz = "-"
else:
    strtz = "+"
offset = abs(offset)

if offset % 3600 == 0:
    strtz += str(offset // 3600)
else:
    if len(str(offset % 3600 // 60)) == 2: strtz += str(offset // 3600) + ":" + str(offset % 3600 // 60)
    else: strtz += str(offset // 3600) + ":0" + str(offset % 3600 // 60)

ret = "🌍 Локация: " + geo[2] + "\n🕒 Текущие дата и время: " + weekday(dt.isoweekday()).lower() + ", " + dt.strftime("%d.%m.%Y %H:%M:%S") + "\n\n🌐 Часовой пояс: UTC" + strtz + "\n🤖 Unixtime: " + str(round(dt.timestamp())) + "\n⌚ По UTC сейчас " + weekday(utcdt.isoweekday()).lower() + ", " + utcdt.strftime("%d.%m.%Y %H:%M:%S")
message(ret, reply=True)
try:
    del userinfo
except:
    pass
del geo
del dt
del utcdt
del strtz
del ret
