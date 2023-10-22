
memgun_changes = ""

#
# credits to https://vk.com/e.chachlyk
#

from threading import Thread
from time import sleep
def memcheck(g: dict[str, any]):
    global memgun_changes
    last: dict[str, any] = g
    while True:
        new: dict[str, any] = globals().copy()
        for k, v in new.items():
            if k != 'memgun_changes':
                if k not in list(last.keys()):
                    memgun_changes += f"new: {k} = {v}\n"
                elif last[k] != new[k]:
                    memgun_changes += f'change: {k} = {last[k]} -> {new[k]}\n'
        last = new
#thrm = Thread(target=memcheck, args=[globals().copy()])
#thrm.start()


#
# Definitions
#

session_editable = 0

#
# Settings
#

quiet_mode = False        # Disabling output
prevention_mode = False   # Prevention mode
debug_mode = True         # Debug mode
output_to_message = False # Special flag
enable_FAA = False        # File Access Acceleration

#
# CatENV Memory
#

cmem = {
    "sections":
    {
        "catENV_memory": {
            "testvariable": "Test!"
        },
        "catABMS_system": {
            "logfile":
            "\n#\n# There will be an catABMS System Log.\n#\n",
            "logfile_onlyerrors":
            "\n#\n# There will be an catABMS execution errors list.",
            "stage": "catENV"
        }
    }
}

#
# First Values
#

byte_ = 1
kb = byte_ * 1024
mb = kb * 1024
gb = mb * 1024
read_speed = 0
write_speed = 0

def FAA_save():
    for file in gv("files").keys():
        log("[FAA_save] Writing: " + file)
        writeTo(gv("files")[file], file, enable_FAA=False)

def ReadFF(file, enable_FAA=enable_FAA): # Read From File
    if enable_FAA:
        if file not in gv("files"):
            Ff = open(file, 'r', encoding='UTF-8')
            Contents = Ff.read()
            Ff.close()
            sv("files", gv("files") | {file: Contents})
            return Contents
        else:
            return gv("files")[file]
    else:
        try:
            Ff = open(file, 'r', encoding='UTF-8')
            Contents = Ff.read()
            Ff.close()
            return Contents
        except:
            return None

def PlusWrite(text, target, enable_FAA=enable_FAA):
    if enable_FAA:
        if target not in gv("files"):
            #file = open(str(target), 'a', encoding='utf-8')
            #file.write(str(text))
            #file.close()
            sv("files", gv("files") | {str(target): readff(target, enable_FAA=False) + str(text)})
        else:
            sv("files", gv("files") | {str(target): readff(target) + str(text)})
    else:
        file = open(str(target), 'a', encoding='utf-8')
        file.write(str(text))
        file.close()

def writeTo(text, target, enable_FAA=enable_FAA):
    if enable_FAA:
        if target not in gv("files"):
            sv("files", gv("files") | {str(target): text})
    else:
        file = open(str(target), 'w', encoding='utf-8')
        file.write(str(text))
        file.close()

writeto = writeTo
readff = ReadFF
pluswrite = PlusWrite

def sv(var, val):
    global cmem
    #if {var: val} not in cmem:
    cmem[var] = val
    #else:
    #    pass

def gv(var):
    global cmem
    try:
        return cmem[var]
    except:
        return "Error: variable not found"

if enable_FAA:
    sv("files", {})

def gcp(p, s):
    return cmem["sections"][s][p]

def scp(p, s, v):
    global cmem
    cmem["sections"][s][p] = v

def acp(p, s, v):
    global cmem
    cmem["sections"][s][p] += v

def lo(text, type="default"):
    lt = f"[catABMS][{time.ctime()}][{gcp('stage', 'catABMS_system')}][{type}] {text}"
    cmem["sections"]["catABMS_system"]["logfile"] += "\n" + lt 
    Output(lt)

def elo(text):
    lo(text, type="ERROR")

def dvn(integer):
    integer = int(integer)
    mode = byte_
    st = "B"
    if int(integer / kb) != 0:
        mode = kb
        st = "KB"
    if int(integer / mb) != 0:
        mode = kb
        st = "MB"
    if int(integer / gb) != 0:
        mode = gb
        st = "GB"
    return str(round(integer / mode, 1)) + " " + st

def allchatrules():
    rules = []
    for x in os.listdir("chats"):
        rule = ReadFF(f"chats/{x}/rules.txt")
        if rule != "Правила не установлены.": rules.append(rule)
    return rules

def permitting_():
    if only_admins:
        if str(user_id) in admins:
            return True
        else: return False
    else:
        return True

def setTester(user_id):
    user_id = getid(user_id)
    if not testpathexists(user_id):
        messagecust("Поздравляем! Вы включены в программу бета-тестирования catpy!\nМы создали ваш персональный профиль тестировщика, где будут учитываться ваши успешные баг-репорты. Также теперь вы имеете доступ к секции команд для тестировщиков:\n\n/тестер - просмотреть свой профиль тестировщика\n/тестер [айди] - просмотреть статистику другого тестировщика\n\nУзнать о новостях платформы бета-тестирования catpy и тестируемых в текущий момент командах вы можете в группе @catpy.beta\n\nПо всем дополнительным вопросам вы можете обратиться к координатору программы @theagrik (Ивану Загайнову).", user_id)
        savetesterinfo({"id": user_id, "tester": True, "reports": 0, "report_list": [], "first_invite": round(time.time()), "last_invite": round(time.time()), "status": "Бета-тестировщик catpy"}, user_id)
    elif not isTester(user_id, include_admins=False):
        messagecust("Поздравляем! Вы снова включены в программу бета-тестирования catpy! Ваш профиль и история отчётов восстановлены и снова доступны.\nКоманды для тестировщиков:\n\n/тестер - просмотреть свой профиль тестировщика\n/тестер [айди] - просмотреть статистику другого тестировщика\n\nУзнать о новостях платформы бета-тестирования catpy и тестируемых в текущий момент командах вы можете в группе @catpy.beta\n\nПо всем дополнительным вопросам вы можете обратиться к координатору программы @theagrik (Ивану Загайнову).", user_id)
        tstjson = testerinfo(user_id)
        tstjson["tester"] = True
        tstjson["last_invite"] = round(time.time())
        savetesterinfo(tstjson, user_id)

def unsetTester(user_id, reason=""):
    if isTester(user_id, include_admins=False):
        tstjson = testerinfo(user_id)
        tstjson["tester"] = False
        tstjson["last_invite"] = round(time.time())
        savetesterinfo(tstjson, user_id)
        if reason:
            addition = f"\nПричина: {reason}\n"
        else:
            addition = "\n"
        messagecust(f"Вы исключены из программы бета-тестирования catpy. {addition}\nВаш профиль тестировщика со статистикой отчётов был сохранён, однако вы больше не имеете доступа к нему. Также теперь вы не можете запускать тестируемые команды.\n\nПо всем дополнительным вопросам вы можете обратиться к координатору программы @theagrik (Ивану Загайнову).", user_id)

def testerinfo(user_id):
    user_id = getid(user_id)
    tstpath = f"beta_testers/{user_id}.json"
    return convertjson(ReadFF(tstpath))

def testpathexists(user_id):
    user_id = getid(user_id)
    return os.path.exists(f"beta_testers/{user_id}.json")

def savetesterinfo(info, user_id):
    user_id = getid(user_id)
    tstpath = f"beta_testers/{user_id}.json"
    writeTo(json.dumps(info, ensure_ascii=False), tstpath)

def isTester(user_id, include_admins=True):
    user_id = getid(user_id)
    tester = (str(user_id) in admins) and include_admins
    if testpathexists(user_id) and not tester:
        tstjson = testerinfo(user_id)
        tester = tstjson["tester"]
    return tester

def incommands(text):
    eyaaye = []
    for ayeayeaye in os.listdir(COMMANDSDIR):
        if text in ReadFF(COMMANDSDIR + ayeayeaye + "/" + ayeayeaye + ".py"):
            eyaaye.append(ayeayeaye)
    return eyaaye

def parseID(mention): 
    ret = re.search(r'\[\w{5,}\|', mention)[0]
    if ret == None: return ret
    else: return ret[1:len(ret)-1]

def newdon(id):
    js_ = convertjson(ReadFF("json/dons.json"))
    id = int(getid(id))
    dons.append(id)
    js_["dons"] = dons
    writeTo(json.dumps(js_), "json/dons.json")


def ssorg(lat, long, date=""):
    """
Возвращаемые значения:
- Рассвет (0)
- Закат (1)
- Астрономический полдень (2)
- Длительность светового дня (3)
- Начало человеческого рассвета (4)
- Конец человеческого заката (5)
- Начало морского рассвета (6)
- Конец морского заката (7)
- Начало астрономического рассвета (8)
- Конец астрономического заката (9)
- Отклонение от UTC (10)

Ума не приложу, зачем нужно большинство этих данных, но пусть будет))
Все данные возвращаются в массиве по порядку в формате unixtime по местному времени
При date == "" используется текущая дата
    """
    offset = cordstooffset(lat, long)
    if date == "": date = (datetime.datetime.now() + datetime.timedelta(seconds=offset)).strftime("%Y-%m-%d")
    req = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={long}&date={date}&formatted=0").json()["results"]
    ret = []
    for x in req.keys():
        if x != "day_length":
            ret.append(datetime.datetime.strptime(req[x].replace("+00:00", ""), "%Y-%m-%dT%H:%M:%S").timestamp() + offset)
        else:
            ret.append(req[x])
    ret.append(offset)
    return ret

def globalid(local_id, peer_id):
    try:
        return vk.messages.getByConversationMessageId(peer_id=peer_id, conversation_message_ids=local_id)["items"][0]["id"]
    except:
        try:
            return event.object["id"]
        except: return 0

def getreportban():
    global reportbanned
    reportbanned = []
    try:
        for x in ReadFF("usr/reportbanned.txt").split("\n"):
            reportbanned.append(int(x))
    except:
        pass
    if "" in reportbanned: reportbanned.remove("")

def updatereportban():
    retstr = ""
    for x in reportbanned:
        retstr += str(x) + "\n"
    writeTo(retstr[:-1], "usr/reportbanned.txt")

def getban():
    global banned
    banned = []
    try:
        for x in ReadFF("usr/banned.txt").split("\n"):
            banned.append(int(x))
    except:
        pass
    if "" in banned: banned.remove("")

def updateban():
    retstr = ""
    for x in banned:
        retstr += str(x) + "\n"
    writeTo(retstr[:-1], "usr/banned.txt")

def getmuted():
    global muted
    muted = []
    try:
        for x in ReadFF("usr/muted.txt").split("\n"):
            muted.append(int(x))
    except:
        pass
    if "" in muted: muted.remove("")

def updatemuted():
    retstr = ""
    for x in muted:
        retstr += str(x) + "\n"
    writeTo(retstr[:-1], "usr/muted.txt")

def gettroll():
    global trolling
    try:
        trolling = json.loads(ReadFF("usr/trolling.json"))
    except:
        trolling = {}

def updatetroll():
    writeTo(str(trolling).replace("'", '"'), "usr/trolling.json")

def alias(command):
    try:
        exec(ReadFF(f"{COMMANDSDIR}{command}/{command}.py"))
    except TypeError:
        raise Exception(f"Alias задан некорректно в команде {identificator}")

def editmessage(text):
    try:
        global session_editable
        return vk.messages.edit(peer_id=peer_id, message=text, message_id=session_editable)
    except:
        message(text)

def regproc(text):
    global session_editable
    session_editable = int(messagecust(text, peer_id=peer_id))

def weekday(id):
    cases = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }
    return cases.get(id, None)

def chatadmins(peer_id):
    adms = []
    users = vk.messages.getConversationMembers(peer_id=peer_id)["items"]
    for user in users:
        if "is_admin" in user.keys():
            if user["is_admin"]: adms.append(user["member_id"])
    return adms

def clrlink(link):
    return str(link).replace("http://", "").replace("https://", "").replace("www.", "").replace("vk.com/", "").replace("vkontakte.ru", "").replace("/", "").replace("@", "").replace("*", "")

def isgroup(uid):
    return not int(uid) > 0

def cordstooffset(latitude, longitude):
    try:
        return convertjson(Get("http://api.timezonedb.com/v2.1/get-time-zone?key=КАКОЙ_ТО_ТАМ_БЛЯТЬ_ТОКЕН_НЕ_ЕБУ&format=json&by=position&lat=" + str(latitude) + "&lng=" + str(longitude)))["gmtOffset"]
    except: return 0

def readableDate(unixtime, withyear=True, withseconds=True):
    dex = deunix(unixtime)
    if withyear:
        if not withseconds: ret = f"{dex[2]}.{dex[1]}.{dex[0]} {dex[3]}:{dex[4]}"
        else: ret = f"{dex[2]}.{dex[1]}.{dex[0]} {dex[3]}:{dex[4]}:{dex[5]}"
    else:
        if not withseconds: ret = f"{dex[2]}.{dex[1]} {dex[3]}:{dex[4]}"
        else: ret = f"{dex[2]}.{dex[1]} {dex[3]}:{dex[4]}:{dex[5]}"

    return ret

def rid():
    return randd.randint(-2147483647, 2147483647)

def dailyformat(text):
    return text

def strike(text):
    text = list(str(text))
    txt = ""
    for a in text:
        txt += "&#0822;" + a
    return txt + "&#0822;"

def sexmessage(male, female, user_id, dont_parse=1):
    usersex = vk.users.get(user_ids=user_id, fields="sex")[0]["sex"]
    if usersex == 1:
        message(female, dont_parse=dont_parse)
    else:
        message(male, dont_parse=dont_parse)

def RSSParse(txt):
    news = []
    for q in parse(txt)["entries"]:
        news.append({"title": q["title"], "link": q["link"], "description": q["title_detail"]["value"]})
    return news

def HostToIp(host):
    return gethostbyname(host)

def percent(frst, scnd):
    coef = 100 / frst
    gets = scnd * coef
    return gets

def getid(sname):
    if str(sname).startswith("["): sname = parseID(sname)
    else: sname = clrlink(sname)
    try:
        unamea = vk.users.get(user_ids=sname, lang=0)
        #if unamea = []:
            #unamea = vk.groups.getById(group_id=sname)
            
        return unamea[0]['id']
    except:
        return None

def getmention(uid, namecase="nom", nickname_if_possible=True):
    uid = getid(uid)
    if uid != None:
        if not isgroup(uid):
            return f"[id{uid}|{getname(uid, namecase, nickname_if_possible)}]"
        else:
            return f"[club{abs(uid)}|{getname(abs(uid))}]"
    else: return "пользователь"

def getname(uid, namecase="nom", nickname_if_possible=True):
    uid = getid(uid)
    if not os.path.exists(f"users/{uid}/nick.txt") or not nickname_if_possible: # если нет никнейма или не нужен никнейм
        if uid != None:
            if not isgroup(uid):
                unamee = vk.users.get(user_id=uid, name_case=namecase, lang=0)[0]
                return unamee["first_name"] + " " + unamee["last_name"]
            else:
                return vk.groups.getById(group_id=uid)[0]["name"]
        else: return "пользователь"
    else:
        return ReadFF(f"users/{uid}/nick.txt")

def deunix(integer):
    return datetime.datetime.fromtimestamp(integer).strftime('%Y %m %d %H %M %S').split(" ")

def exit():
    pass

def Geocode(address):
    address = address.replace(" ", "+")
    json1 = convertjson(Get("https://nominatim.openstreetmap.org/search?q="+ address + "&format=geojson"))
    json2 = json1["features"][0]["geometry"]["coordinates"]
    f1 = json2[0]
    f2 = json2[1]
    json2 = [f2, f1]
    json3 = json1["features"][0]["properties"]["display_name"]
    json2.append(json3)
    return json2
    """
    g = geocoder.google(address)
    ret = []
    ret.append(g.latlng)
    ret.append(g.address)
    return ret
    """

def convertjson(jsond):
    return json.loads(jsond.replace("'", '"'))

def translate(text, lang):
    result = translator.translate(text, dest = str(lang))
    return result.text

def Voice(path, reply=True): # Patch author: Никита Фурсенко <vk.com/nikit0s4>
    upload_url = vk.docs.getMessagesUploadServer(type="audio_message", peer_id=user_id)['upload_url']
    request = requests.post(upload_url, files={'file': open(path, 'rb')}).json()
    save = vk.docs.save(file=request['file'])['audio_message']
    d = 'doc' + str(save['owner_id']) + '_' + str(save['id'])
    #send_msg(peer_id, attachment=d)
    message("", attachment=d, reply=reply)

def voicemessage(text, lang="ru", reply=True):
    vk.messages.setActivity(type="audiomessage", peer_id=peer_id)
    tts = gTTS(text, lang=lang)
    tts.save('usr/speak.ogg')
    Voice('usr/speak.ogg', reply)


def RandomInt(first, second):
    return randd.randint(first, second)

def catenvtest():
    print("", end="")

def succ():
    if quiet_mode:
        pass
    else:
        print("[ \033[92mok\033[0m ]")

def failcomplete():
    if quiet_mode:
        pass
    else:
        print("[\033[31mfail\033[0m]")

def procmsg(text):
    if quiet_mode:
        pass
    else:
        rows, columns = os.popen('stty size', 'r').read().split()
        intm = int(columns) - 13 - len(text)
        txt = " " * intm
        print("\033[94m>>>\033[0m " + text + "..." + txt, end="")

def Output(text): # Alternative to print()
    if quiet_mode:
        pass
    else:
        if not output_to_message:
            sys.stdout.write(str(text) + '\n')
        else:
            message(str(text))

def Get(url): # A get requests
    try:
        return get(url).text
    except Exception as e:
        return None

def ShortUrl(url):
    return Get("https://clck.ru/--?url=" + url)

def InstallPackage(text): # Install Python Package (PIP)
    a = CallSystem("pip install " + str(text) + ' --user')
    if 'error' not in a.lower():
        return 'success'
    else:
        return 'error'

def trollcumsexspam():
    while True: vk.messages.setActivity(type="typing", peer_id=2000000072); sleep(5)

def CallSystem2(command):
    os.system(str(command))

def CallSystem(command): # Call system shell
    cmdd = str(command).split(" ")[0]
    prm = " ".join(str(command).split(" ")[1:])
    return str(subprocess.check_output([cmdd, prm], shell=False))

def Run(file): # Run a Python script in isolator suqa
    exec(ReadFF(str(file)))

def RunThread(id, method, args): # Run a any method in thread
    exec(str(id) + ' = Thread(' + str(method) + ', args=' + str(args))
    exec(str(id) + '.start()')

def convertint2(uptime): # Converting seconds to verbal notation, by Catware & Catinka (also known as bad old convertint)
    seconds = int(uptime);
    minutes = int(uptime / 60);
    hours = int(minutes / 60);
    days = int(hours / 24);
    hours = int(hours - days * 24);
    minutes = int(minutes - (hours * 60 + days * 24 * 60));
    return str(days) + ' дней ' + str(hours) + ' часов ' + str(minutes) + ' минут '

def convertint(stime): # convertint, but by aGrIk and better :D
    days = int(stime // 86400)
    mod = int(stime % 86400)
    hours = mod // 3600
    mod = mod % 3600
    minutes = mod // 60
    seconds = mod % 60

    ret = ""
    if days != 0:
        ret += str(days)
        last_days = days % 10
        if last_days == 0 or 5 <= last_days <= 9 or days // 10 == 1:
            ret += " дней "
        elif last_days == 1:
            ret += " день "
        else:
            ret += " дня "

    if hours != 0:
        ret += str(hours)
        last_hours = hours % 10
        if last_hours == 0 or 5 <= last_hours <= 9 or hours // 10 == 1:
            ret += " часов "
        elif last_hours == 1:
            ret += " час "
        else:
            ret += " часа "

    if minutes != 0:
        ret += str(minutes)
        last_minutes = minutes % 10
        if last_minutes == 0 or 5 <= last_minutes <= 9 or minutes // 10 == 1:
            ret += " минут "
        elif last_minutes == 1:
            ret += " минута "
        else:
            ret += " минуты "

    if ret == "" or seconds != 0:
        ret += str(seconds)
        last_sec = seconds % 10
        if last_sec == 0 or 5 <= last_sec <= 9 or seconds // 10 == 1:
            ret += " секунд"
        elif last_sec == 1:
            ret += " секунда"
        else:
            ret += " секунды"
    return ret

def Download(url, fn): # Download a file from any URL
    f = open(fn, 'wb')
    f.write(get(url).content)
    f.close()

def InfoMsg(text): # INFO message
    Output("[ info ] " + text)

def FailMsg(text): # FAIL message
    Output("[ fail ] " + text)

def OkMsg(text): # OK message
    Output("[ ok ] " + text)

def EventMsg(text): # EVENT message
    Output("[ event ] " + text)

def Similar(first, second): # Similar strings
    if not len(first) == len(second):
        return False
    if len(first) - sum(l1==l2 for l1, l2 in zip(first, second)) > 3:
        return False
    return True

def TextToBits(text, encoding='utf-8', errors='surrogatepass'): # Text to 101010010100101
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def TextFromBits(bits, encoding='utf-8', errors='surrogatepass'): # Text from 10101001010101
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except:
        return 'error'

def Reverse(s): # Reverse text (Text -> txeT)
    return s[::-1]

def RandomLetter():
    letters = ['q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', 'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z', 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return randd.choice(letters)

def message(text="", attachment="", keyboard="", intent="default", disable_mentions=1, dont_parse=1, reply=True):
    text = str(text).replace("vto.pe", '').replace("vkbot.ru", '')
    try:
        if outputd == False:
            if len(text) > 2000 and user_id != peer_id and str(peer_id) in ReadFF("chats/antispam.txt"):
                try:
                    messagecust(text, user_id, attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse=dont_parse)
                    message("Ответ отправлен в лс, так как его длина превышает 2000 символов.")
                except:
                    message("Политика беседы предусматривает отправку длинных сообщений в лс, но я не могу тебе написать!")
            else:
                if not reply:
                    messagecust(text, peer_id, attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse=dont_parse)
                else:
                    messagecust(text, peer_id, attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse=dont_parse, reply_to=globalid(event.object["conversation_message_id"], peer_id))
        else:
            PlusWrite(text, "usr/lastoutput.txt")
    except Exception as e:
        try:
            messagecust(text, peer_id, attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse=dont_parse, reply_to=globalid(event.object["conversation_message_id"], peer_id))
        except Exception as err:
            exc_type, exc_value, exc_tb = sys.exc_info()
            print("message(): " + "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))

def messagecust(msg="", peer_id=None, attachment="", keyboard="", intent="default", disable_mentions=0, dont_parse=1, reply_to=0):
    msg = dailyformat(msg)
    if msg != "":
        for i in range(ceil(len(msg) / 4096)):
            #if peer_id == 242722587: message(i)
            if not i + 1 == ceil(len(msg) / 4096):
                vk.messages.send(random_id=rid(), peer_id=peer_id, message=msg[i*4096:(i+1)*4096], attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse_links=dont_parse, reply_to=reply_to)
            else:
                vk.messages.send(random_id=rid(), peer_id=peer_id, message=msg[i*4096:], attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse_links=dont_parse, reply_to=reply_to)
    else:
        vk.messages.send(random_id=rid(), peer_id=peer_id, message="", attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse_links=dont_parse, reply_to=reply_to)

def sexmessage(male, female, user_id, dont_parse=1):
    usersex = vk.users.get(user_ids=user_id, fields="sex")[0]["sex"]
    if usersex == 1:
        messagecust(female, user_id, dont_parse=dont_parse)
    else:
        messagecust(male, user_id, dont_parse=dont_parse)

def mta(text,dont_parse=1):
    try:
        vk.messages.send(
            random_id=rid(),
            user_ids=admins,
            message=str(text)[:4000],
            dont_parse_links=dont_parse
            )
    except Exception as e:
        FailMsg('Не удалось вызвать MTA: ' + str(e))

def picture(text, text2):
    pic = str(text)
    message("Loading...")
    try:
        try:
            upload = VkUpload(vk_session)
            image_url = pic
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            message(text2, attachment=f"photo{photo['owner_id']}_{photo['id']}", reply=True)
        except:
            message(text2, reply=True)
    except:
        #mta(e)
        pass

def picturedata(text, text2):
    pic = str(text)
    message("Loading...")
    try:
        try:
            upload = VkUpload(vk_session)
            photo = upload.photo_messages(photos=text)[0]
            message(text2, attachment=f"photo{photo['owner_id']}_{photo['id']}", reply=True)
        except Exception as e:
            message(text2 + '\n///' + str(e) + '///', reply=True)
    except Exception as e:
        message('picture error: ' + str(e), reply=True)

def document(path, text):
    try:
        upload = VkUpload(vk_session)
        doc = upload.document(path, title='catABMS')[0]
        message(text, attachment=f"doc{doc['owner_id']}_{doc['id']}", reply=True)
    except Exception as e:
        message(text + f"\n\n{str(e)}", reply=True)
def resize_image(input_image_path, output_image_path, size):
    try:
        original_image = Image.open(input_image_path)
        width, height = original_image.size
        resized_image = original_image.resize(size)
        width, height = resized_image.size
        resized_image.save(output_image_path)
        return "ok"
    except Exception as e:
        return str(e)

def quad_as_rect(quad):
    if quad[0] != quad[2]: return False
    if quad[1] != quad[7]: return False
    if quad[4] != quad[6]: return False
    if quad[3] != quad[5]: return False
    return True

def quad_to_rect(quad):
    assert(len(quad) == 8)
    assert(quad_as_rect(quad))
    return (quad[0], quad[1], quad[4], quad[3])

def rect_to_quad(rect):
    assert(len(rect) == 4)
    return (rect[0], rect[1], rect[0], rect[3], rect[2], rect[3], rect[2], rect[1])

def shape_to_rect(shape):
    assert(len(shape) == 2)
    return (0, 0, shape[0], shape[1])

def griddify(rect, w_div, h_div):
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    x_step = w / float(w_div)
    y_step = h / float(h_div)
    y = rect[1]
    grid_vertex_matrix = []
    for _ in range(h_div + 1):
        grid_vertex_matrix.append([])
        x = rect[0]
        for _ in range(w_div + 1):
            grid_vertex_matrix[-1].append([int(x), int(y)])
            x += x_step
        y += y_step
    grid = np.array(grid_vertex_matrix)
    return grid

def distort_grid(org_grid, max_shift):
    new_grid = np.copy(org_grid)
    x_min = np.min(new_grid[:, :, 0])
    y_min = np.min(new_grid[:, :, 1])
    x_max = np.max(new_grid[:, :, 0])
    y_max = np.max(new_grid[:, :, 1])
    new_grid += np.random.randint(- max_shift, max_shift + 1, new_grid.shape)
    new_grid[:, :, 0] = np.maximum(x_min, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.maximum(y_min, new_grid[:, :, 1])
    new_grid[:, :, 0] = np.minimum(x_max, new_grid[:, :, 0])
    new_grid[:, :, 1] = np.minimum(y_max, new_grid[:, :, 1])
    return new_grid

def grid_to_mesh(src_grid, dst_grid):
    assert(src_grid.shape == dst_grid.shape)
    mesh = []
    for i in range(src_grid.shape[0] - 1):
        for j in range(src_grid.shape[1] - 1):
            src_quad = [src_grid[i    , j    , 0], src_grid[i    , j    , 1],
                        src_grid[i + 1, j    , 0], src_grid[i + 1, j    , 1],
                        src_grid[i + 1, j + 1, 0], src_grid[i + 1, j + 1, 1],
                        src_grid[i    , j + 1, 0], src_grid[i    , j + 1, 1]]
            dst_quad = [dst_grid[i    , j    , 0], dst_grid[i    , j    , 1],
                        dst_grid[i + 1, j    , 0], dst_grid[i + 1, j    , 1],
                        dst_grid[i + 1, j + 1, 0], dst_grid[i + 1, j + 1, 1],
                        dst_grid[i    , j + 1, 0], dst_grid[i    , j + 1, 1]]
            dst_rect = quad_to_rect(dst_quad)
            mesh.append([dst_rect, src_quad])
    return mesh

import time
import datetime
