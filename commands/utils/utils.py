# CatOS-type package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'utils'
command_ru = 'утил'
description = 'Утилиты для админов'

if str(user_id) in admins:
    try:
        parray = parameter.split(" ")
        parray[0] = parray[0].lower()
        if parray[0] == "":
            message("""Утилиты для администрации бота:

            Утил подгрузить [путь к команде] - введение команды в строй без перезагрузки;

            Утил вгрузить [raw dpaste] [путь к команде] - вгрузка команды из dpaste;

            Утил выгрузить [путь к команде] - выгружает команду в dpaste;

            Утил катенв - переподгружает CatENV;

            Утил рестарт - переподгружает компоненты ядра: пакеты команд, CoreRC и сервисы;

            Утил коррц - переподгружает CoreRC-модули;

            Утил команда [идентификатор] - генерирует пакет команды;

            Утил подсчётстрок - подсчитывает кодовую базу catpy;

            Утил журналошибок - показывает последние ошибки;

            Утил репортбан [айди] - банит/разбанивает возможность использования репортов пользователем;

            Утил репортбанлист - выводит список заблокированных в репорте пользователей;

            Утил бан [айди] - банит/разбанивает пользователей;

            Утил банлист - выводит список заблокированных пользователей;

            Утил бред - шлёт на Catware AI запрос на переподгрузку текстов бредогенератора;

            Утил мут [айди] - кидает клоуна в мут или убирает оттуда;

            Утил мутлист - выводит список лолчелтывмуте;

            Утил затроллить [айди] (текст) - начинает/перестаёт троллить пользователя текстом;

            Утил тролльлист - выводит список троллящихся пользователей;

            Утил тестер [айди] (текст) - добавляет/убирает пользователя в бета-тестировании, текст отправляется как причина исключения;

            Утил багрепорт [айди] - начисляет успешный багрепорт;

            Утил тестеры - выводит список бета-тестировщиков;
            
            Утил оборона - включает/отключает защищённый режим;
            
            Утил отключить - завершает работу CatABMS""", reply=True)
        if parray[0] == "команда" and len(parray) > 1:
            cmdname = " ".join(parray[1:])
            os.mkdir(f"{COMMANDSDIR}{cmdname}")
            js = {"author": "undefined", "mode": "=", "identificator": cmdname, "command_ru": "undefined", "description": "undefined"}
            js["testing"] = False
            js["hide"] = True
            js["restricted"] = False
            js["disabled"] = True
            writeTo("", f"{COMMANDSDIR}{cmdname}/{cmdname}.py")
            writeTo(json.dumps(js, ensure_ascii=False), f"{COMMANDSDIR}{cmdname}/{cmdname}.json")
            message("Успешно!", reply=True)

        if parray[0] == "админ" and len(parray) == 2:
            newadmstr = getid(clrlink(parray[1]))
            if str(newadmstr) not in admins.split("1"):
                mta(f"ВНИМАНИЕ! СООБЩЕНИЕ СИСТЕМЫ БЕЗОПАСНОСТИ! Администратор {getmention(user_id)} назначает {getmention(newadmstr, 'gen')} администратором catpy! Это позволит {getmention(newadmstr, 'gen')} вызывать ВСЕ команды и использовать утилиты, в том числе и исключать администраторов. Если вы считаете, что назначение не было санкционировано, отмените назначение командой /утил админ {newadmstr}.")
                admins += f",{newadmstr}"
                admins = admins.replace(",,", ",")
                writeTo(",".join(admins), "admins.txt")
                message(f"Внимание! Вы назначили {getmention(newadmstr, namecase='gen')} администратором catpy. Новый администратор имеет доступ ко всем командам catpy. Убедитесь, что данное назначение безопасно и целесообразно. О данном назначении сообщено всей администрации. Отменить назначение можно, введя /утил админ {newadmstr}", reply=True)
                messagecust("Привет! Кажется, тебя назначили администратором технической части бота catpy! Отныне ты можешь использовать администраторские утилиты catpy. Надеюсь, что тебя уже научили это применять, но всё же запомни 3 правила:\n\n1) Не применяй наработки catpy во вред кому-то или catpy\n2) Думай, прежде чем написать\n3) С большой властью приходит большая ответственность\n\nУдачи!", newadmstr)
            else:
                if str(newadmstr) not in "458828641,597100871,242722587".split("."):
                    admins = admins.replace(f",{newadmstr}", "").replace(f"{newadmstr},", "")
                    writeTo(",".join(admins), "admins.txt")
                    messagecust("Ты был исключён из администрации catpy.", newadmstr)
                    mta(f"ВНИМАНИЕ! СООБЩЕНИЕ СИСТЕМЫ БЕЗОПАСНОСТИ! Администратор {getmention(user_id)} исключает {getmention(newadmstr, 'gen')} из списка администраторов. ")
                    message(f"{getmention(newadmstr)} больше не является админом catpy.", reply=True)
                else:
                    message(f"Вы не имеете права исключить {getmention(newadmstr, 'gen')} из числа администраторов catpy.", reply=True)

        if parray[0] == "журналошибок":
            message("Журнал ошибок.\n\n" + system_errors, reply=True)

        if parray[0] == "коррц":
            rcs = []
            loaded = 0
            notloaded = 0
            message("Подгружаю CoreRC-модули...")
            for x in os.listdir("corerc"):
                try:
                    rcs.append(ReadFF('corerc/' + x))
                    loaded += 1
                except Exception as e:
                    careless += 1
                    notloaded += 1
                systemcare += 1
            message(f"Готово! Успешно подгружено: {loaded}, возникла ошибка при подгрузке: {notloaded}")

        if parray[0] == "подгрузить":
            cmd = parray[1]
            try:
                message("Загрузка команды " + cmd[:-3], reply=True)
                cmdjs = convertjson(ReadFF(f"{COMMANDSDIR}{cmd[:-3]}/{cmd[:-3]}.json"))
                if not cmdjs["disabled"]:
                    authors.append(cmdjs["author"])
                    modes.append(cmdjs["mode"])
                    ids.append(cmdjs["identificator"])
                    commands.append(cmdjs["command_ru"])
                    descs.append(cmdjs["description"])
                    succ()
                    systemcare += 1
            except:
                    message("Не удалось загрузить команду " + cmd[:-3])
            message("Выполнение системного сервиса...")
            exec(ReadFF("services/commands.py"))
            message("Выполнено!")

        if parray[0] == "рестарт":
            message("Перезагружаюсь...")
            exec(ReadFF("faststart.py"))

        if parray[0] == "вгрузить":
            writeTo(Get(parray[1]), parray[2])
            message("Код успешно вгружен, перезагрузите бота, чтобы изменения вступили в силу.", reply=True)

        if parray[0] == "катенв":
            message("Подгружаю окружение...", reply=True)
            try:
                catenv = ReadFF("catenv.py")
                exec(catenv)
                __catenv__ = catenv
                message("Успех!")
            except Exception as e:
                exc_type, exc_value, exc_tb = sys.exc_info()
                exec(__catenv__)
                v = "\n"
                message(f"Во время инициализации нового CatENV произошла ошибка. Откат на предыдущий CatENV произведён.\n\n{v.join(traceback.format_exception(exc_type, exc_value, exc_tb))}")

        if parray[0] == "бред":
            message("Инициализирую перезагрузку бреда...", reply=True)
            req = requests.get("http://artificalintellect.pythonanywhere.com/breadrestart?access_token=OUJFVHLKRUHlWURHGKURGFkygsRKHFLSEHUFJjKJFhJLSLHRFJ<SHFGKJSDGFKJHGSDFhjsdkfhbjSDHGFukSDF")
            if req.text.startswith("ok"): message("Успех!")
            else: message(req.text, reply=True)

        if parray[0] == "выгрузить":
            message("Выгрузка кода:\n" + requests.post("http://dpaste.com/api/v2/", data={"content": ReadFF(" ".join(parray[1::])), "title": parameter + " file", }).text + "\nИстекает через 7 дней", reply=True)

        if parray[0] == "подсчётстрок":
            lines = 0
            baits = 0
            message("Начинается подсчёт...", reply=True)

            dirs = ["corerc", "services", "configs", "experimental", "lib"]
            for a in dirs:
                for y in os.listdir(a):
                    lines += len(ReadFF(a + "/" + y).split("\n"))
                    baits += len(ReadFF(a + "/" + y))
            for a in os.listdir(COMMANDSDIR):
                for b in os.listdir(COMMANDSDIR + a):
                    lines += len(ReadFF(COMMANDSDIR + a + "/" + b).split("\n"))
                    baits += len(ReadFF(COMMANDSDIR + a + "/" + b))
            lines += len(ReadFF("core.py").replace("\n\n", "\n").split("\n"))
            lines += len(ReadFF("catenv.py").split("\n"))
            lines += len(ReadFF("start.py").split("\n"))
            baits += len(ReadFF("core.py"))
            baits += len(ReadFF("catenv.py"))
            baits += len(ReadFF("start.py"))
            message("Подсчёт успешен. Кодовая база котопая = " + str(lines) + " строк; общий вес CatABMS: " + dvn(baits), reply=True)
            del lines

        if parray[0] == "репортбан" and len(parray) == 2:
            banid = getid(parray[1])
            if banid != None:
                if banid not in reportbanned:
                    reportbanned.append(banid)
                    updatereportban()
                    message(f"Пользователю {getmention(banid, 'dat')} заблокирована возможность репорта.", reply=True)
                else:
                    reportbanned.remove(banid)
                    updatereportban()
                    message(f"Пользователю {getmention(banid, 'dat')} разблокирована возможность репорта.", reply=True)
            else:
                message("Блокировка не удалась: некорректное id", reply=True)

        if parray[0] == "бан" and len(parray) == 2:
            banid = getid(parray[1])
            if banid != None:
                if banid not in banned:
                    banned.append(banid)
                    updateban()
                    message(f"Пользователь {getmention(banid)} заблокирован.", disable_mentions=1, reply=True)
                else:
                    banned.remove(banid)
                    updateban()
                    message(f"Пользователь {getmention(banid)} разблокирован.", disable_mentions=1, reply=True)
            else:
                message("Блокировка не удалась: некорректное id", reply=True)

        if parray[0] == "мут" and len(parray) == 2:
            banid = getid(parray[1])
            if banid != None:
                if banid not in muted:
                    muted.append(banid)
                    updatemuted()
                    message(f"Пользователь {getmention(banid)} отныне в муте. Клоун......", disable_mentions=1, reply=True)
                else:
                    muted.remove(banid)
                    updatemuted()
                    message(f"Пользователь {getmention(banid)} больше не в муте.", disable_mentions=1, reply=True)
            else:
                message("Замутить не удалось: некорректное id", reply=True)

        if parray[0] == "мутлист":
            getmuted()
            if muted != []:
                ret = f"Список клоунов в муте ({len(muted)}):\n"
                for x in muted:
                    ret += f"{getmention(x)} ({x})\n"
                message(ret, reply=True)
            else: message("В муте никого нет.", reply=True)

        if parray[0] == "затроллить" and len(parray) > 1:
            banid = getid(parray[1])
            if banid != None:
                if str(banid) not in trolling.keys():
                    if len(parray) > 2:
                        trolling.update({str(banid): " ".join(parray[2:])})
                        updatetroll()
                        message(f"Пользователь {getmention(banid)} будет затроллен текстом {' '.join(parray[2:])}", disable_mentions=1, reply=True)
                    else:
                        message("Начать троллить не удалось: не указан текст для троллинга.", reply=True)
                else:
                    del trolling[str(banid)]
                    updatetroll()
                    message(f"Пользователь {getmention(banid)} больше не троллится.", disable_mentions=1, reply=True)
            else:
                message("Начать троллить не удалось: некорректное id", reply=True)

        if parray[0] == "тролльлист":
            gettroll()
            if trolling != {}:
                ret = f"Список троллящихся пользователей ({len(trolling.keys())}):\n"
                for tkey in trolling.keys():
                    tk = int(tkey)
                    ret += f"{getmention(tk)} ({tk}): {trolling[tkey]}\n"
                message(ret, reply=True)
            else: message("Никто не троллится.", reply=True)

        if parray[0] == "банлист":
            getban()
            if banned != []:
                ret = f"Список заблокированных пользователей ({len(banned)}):\n"
                for x in banned:
                    ret += f"{getmention(x)} ({x})\n"
                message(ret, reply=True)
            else: message("Заблокированных пользователей нет.", reply=True)

        if parray[0] == "репортбанлист":
            getreportban()
            if reportbanned != []:
                ret = f"Список заблокированных в репорте пользователей ({len(reportbanned)}):\n"
                for x in reportbanned:
                    ret += f"{getmention(x)} ({x})\n"
                message(ret, reply=True)
            else: message("Заблокированных в репорте пользователей нет.", reply=True)

        if parray[0] == "тестер" and len(parray) >= 2:
            uid = getid(parray[1])
            if not isTester(uid, include_admins=False):
                setTester(uid)
                message(f"Пользователь {getmention(uid)} успешно назначен бета-тестировщиком catpy, уведомление отправлено.")
            else:
                if len(parray) > 2:
                    unsetTester(uid, " ".join(parray[2:]))
                else:
                    unsetTester(uid)
                message(f"Пользователь {getmention(uid)} исключён из бета-тестировщиков catpy, уведомление отправлено.")

        if parray[0] == "багрепорт" and len(parray) == 2:
            uid = getid(parray[1])
            if isTester(uid, include_admins=False):
                tstjson = testerinfo(uid)
                tstjson["reports"] += 1
                savetesterinfo(tstjson, uid)
                message(f"Тестировщику {getmention(uid, 'dat')} начислен 1 успешный багрепорт. Количество успешных багрепортов: {tstjson['reports']}.")
                messagecust(f"Вам начислен 1 успешный багрепорт. Количество успешных багрепортов: {tstjson['reports']}.", uid)
            else:
                message("Пользователь не является тестировщиком.")

        if parray[0] == "тестеры":
            tstrs = []
            for user in os.listdir("beta_testers"):
                user = user.split(".")[0]
                if isTester(user, False): tstrs.append(int(user))
            if len(tstrs) > 0:
                ret = f"Активные участники программы бета-тестирования catpy ({len(tstrs)}):\n"
                for user in tstrs:
                    ret += f"{getmention(user)} ({user})\n"
                message(ret)
            else:
                message("В программе нет ни одного человека.")

        if parray[0] == "оборона":
            if not only_admins:
                only_admins = True
                mta(f"Администратор {getmention(user_id)} ввёл CatABMS в защищённый режим. Система будет реагировать только на сообщения администраторов.")
                message("Защищённый режим включен.")
            else:
                only_admins = False
                mta(f"Администратор {getmention(user_id)} вывел CatABMS из защищённого режима. Система будет реагировать на все сообщения.")
                message("Защищённый режим выключен.")

        if parray[0] == "отключить":
            mta(f"Администратор {getmention(user_id)} отправил сигнал завершения работы CatABMS. Система будет отключена через 10 секунд.")
            message("Система будет отключена через 10 секунд.")
            time.sleep(10)
            succ()
            print("**ЗАВЕРШЕНИЕ РАБОТЫ**")
            sys.setrecursionlimit(100000000)
            def recursion(): recursion()
            recursion()

        if parray[0] == "ник" and len(parray) >= 3:
            uid = getid(parray[1])
            if uid != None:
                if os.path.exists(f"users/{uid}"):
                    newnick = " ".join(parray[2:])
                    if newnick.lower() == "!!сброс!!":
                        try:
                            os.remove(f"users/{uid}/nick.txt")
                            message(f"[id{uid}|юзер] сброшен.. бля точьнее ево ник сброшен корочь в канаву превратился в набор нулей сук ау ауе)))")
                        except:
                            message(f"[id{uid}|камрад] походу без ника сидит... или какой то другой эксепшн... хуй знает я гуль.).))")
                    else:
                        writeTo(newnick, f"users/{uid}/nick.txt")
                        message(f"{getmention(uid, 'dat', False)} присвоен никнейм {' '.join(parray[2:])}")
                else:
                    message("Данного пользователя нет в системе.")
            else:
                message("Пользователя с таким айди не существует.")

        if parray[0] == "вививи":
            parray = parray[1:]
            if parray[0] == "орбиталка":
                parray = parray[1:]
                if parray[0] == "заебенить" and len(parray) == 1:
                    orbital_names = "СЕКС,БЛЯУ,ХУЙ,ПИСЬКА,ГЕЙ,ЧЛЕН,БЛЯЗДЯУ,БЛЯХУЙ,ДРОЧКА,ГАНСЕКС,ЕПТА,СУКА".split(",")
                    orbital_vers = "777,228,1337,666,5 300,123,1488,1211".split(",")
                    message("Начинаю заебенивание орбиталки космическим мусором...")
                    __conversations__ = []
                    for aye in vk.messages.getConversations()["items"]:
                        executing = True
                        try:
                            chat_admins = chatadmins(aye["conversation"]["peer"]["id"])
                        except:
                            chat_admins = []
                            executing = False
                        if aye["conversation"]["peer"]["type"] == "chat": __conversations__.append(aye["conversation"]["peer"]["id"])
                    waste = 69420 + randd.randint(10000, 6000000)
                    name = str(randd.choice(orbital_names)) + "-" + str(randd.choice(orbital_vers))
                    #waste = len(__conversations__)
                    message(f"Собрано {waste} кг космического мусора. Орбитальная пушка \"{name}\" готова к распидорашиванию. Ауе!!!!!!!!!!!")
                if parray[0] == "распидорасить" and len(parray) == 2:
                    uid = getid(parray[1])
                    message("Зарядка пушки калом...")
                    for ayeaye in range(4):
                        message(f"Орбиталка заряжена на {(ayeaye + 1) * 20}%", reply=False)
                        time.sleep(1)
                    message(f"Орбиталка заряжена полностью. Ликвидация {getname(uid, 'gen', False)} к хуям...")
                    time.sleep(randd.randint(1, 10))
                    vk.messages.removeChatUser(member_id=uid, random_id=rid(), chat_id=72)
                    message(f"ОТЧЕТ\n\n {getname(uid, 'nom', False)} был разнесен к хуям успешно.")
                    


    except:
        exc_type, exc_value, exc_tb = sys.exc_info()
        message('Error: \n' + "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)), reply=True)

#hide
