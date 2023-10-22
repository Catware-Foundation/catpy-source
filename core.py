Output("CatABMS Kernel version " + core + " startup...")

lo("Loading library: detectfull", type="Kernel Loader")
exec(ReadFF("lib/detectfull.py"))
#exec(ReadFF("lib/surrogate-manager.py"))
lo("Loading library: CUMv2", type="Kernel Loader")
exec(ReadFF("lib/CUMv2.py"))
lo("Loading library: generrorcode", type="Kernel Loader")
exec(ReadFF('lib/generrorcode.py'))

lo("Starting of legacy logger...", type="Kernel Loader")
system_errors = ""
service_errors = []
corerc_errors = []
execution_errors = []
systemcare = 0
careless = 0

COMMANDSDIR = "commands/"
lo("COMMANDSDIR is " + COMMANDSDIR, type="Kernel Loader")
VCCOMMANDSDIR = "voice/"
lo("VCCOMMANDSDIR is " + VCCOMMANDSDIR, type="Kernel Loader")

peers_list = ReadFF("chats/peers.txt")

lo("Loading commands...", type="Kernel Loader")

for x in os.listdir(COMMANDSDIR):
    try:
        procmsg("Loading: " + x)
        cmdjs = convertjson(ReadFF(f"{COMMANDSDIR}{x}/{x}.json"))
        if not cmdjs["disabled"]:
            authors.append(cmdjs["author"])
            modes.append(cmdjs["mode"])
            ids.append(cmdjs["identificator"])
            commands.append(cmdjs["command_ru"])
            descs.append(cmdjs["description"])
            succ()
            systemcare += 1
        else:
            failcomplete()
            Output(f"Warning: command {cmdjs['command_ru']} is disabled")

    except Exception as e:
        failcomplete()
        Output(e)
        system_errors += "Unable to load command: " + str(e)
        lo("Unable to load command: " + str(e), type="Kernel Loader - ERROR")
        systemcare += 1
        careless += 1

for x in os.listdir(VCCOMMANDSDIR):
    try:
        procmsg("Loading Voice Command: " + x)
        cmdjs = convertjson(ReadFF(f"{VCCOMMANDSDIR}{x}/{x}.json"))
        if not cmdjs["disabled"]:
            vc_authors.append(cmdjs["author"])
            vc_modes.append(cmdjs["mode"])
            vc_ids.append(cmdjs["identificator"])
            vc_commands.append(cmdjs["command_ru"])
            vc_descs.append(cmdjs["description"])
            succ()
            systemcare += 1
        else:
            failcomplete()
            Output(f"Warning: Voice Command - {cmdjs['command_ru']} is disabled.")

    except Exception as e:
        failcomplete()
        Output(e)
        system_errors += "Unable to load voice command: " + str(e)
        lo("Unable to load VCCommand: " + str(e), type="Kernel Loader")
        systemcare += 1
        careless += 1

rcs = []
for x in os.listdir("corerc"):
    try:
        procmsg("CoreRC Module loading: " + x[:-3])
        rcs.append(ReadFF('corerc/' + x))
        succ()
    except Exception as e:
        failcomplete()
        careless += 1
    systemcare += 1

endl = "\n"
services_errors = []

Output("Catware Autostart is starting up...")
for x in os.listdir('services'):
    procmsg("Loading service - " + x[:-3])
    try:
        exec(ReadFF("services/" + x))
        succ()
        systemcare += 1
    except Exception as e:
        systemcare += 1
        careless += 1
        failcomplete()
        system_errors += "Сервис: " + x + ", ошибка: " + str(e) + "\n"
        elo("Service: " + x + ', error: ' + str(e))

__conversations__ = []

Output('CatABMS Kernel loading is done.')

writeTo(time.time(), "start-time.txt")

vk2 = VkApi(token="токен от какой то рандомной юзерки ВК, выполнялся для дополнительных функций, которые нельзя вызвать от групп-токена").get_api()

while True:
    try:
        for x in diff:
            exec(f"del {x}")
    except:
        pass
    old_list = dir()
    old_list.append("old_list")
    old_list.append("diff")
    old_list.append("textic")
    old_list.append("textic_2")
    InfoMsg("Started main cycle")
    if only_admins:
        addition = " (безопасный режим)"
    else:
        addition = ""
    mta(f"""Бот запущен{addition}.
Сервер: {Get("http://ident.me/")}
Операционная система: {osname}
Хостнейм: {os.uname()[1]}""")
    del addition
    try:
        for event in longpoll.listen():
            EventMsg(str(event.type))
            if (event.type == VkBotEventType.MESSAGE_NEW or event.type == VkBotEventType.MESSAGE_EDIT) and not isgroup(event.object["message"]['from_id']):

                event.object = event.object["message"]
                using = False
                outputd = False
                writeTo("", "usr/lastoutput.txt")
                PlusWrite(event.object["text"] + "\n", "usr/bread.txt")
                start = time.time()
                user_id = event.object['from_id']
                peer_id = event.object['peer_id']
                if peer_id not in __conversations__: __conversations__.append(peer_id)
                Output(f"\n\n\n=================================\nNew message from user {getname(user_id)} ({str(user_id)}) in chat {str(peer_id)}\nContents: \"{event.object['text']}\"\nAttachments: {str(len(event.object['attachments']))}")
                if len(event.object["attachments"]) > 0:
                    atchmnts = []
                    for atchmnt in event.object["attachments"]:
                        atchmnts.append(atchmnt["type"])
                    Output("Types of attachments: " + ", ".join(atchmnts) + "\n=================================\n\n")
                    del atchmnt, atchmnts
                else: Output("=================================")

                #Отсутствие текста
                if event.object["text"] == "":
                    try:
                        if event.object["attachments"][0]["audio_message"]["duration"] < 30:
                            Download(event.object["attachments"][0]["audio_message"]["link_mp3"], "file.mp3")
                            sound = AudioSegment.from_mp3("file.mp3")
                            sound.export("file.wav", format="wav")
                            sample_audio = speech_recog.AudioFile('file.wav')

                            with sample_audio as audio_file:
                                audio_content = rec.record(audio_file)
                                textop = rec.recognize_google(audio_content, language="ru-RU").split(" ")
                                if textop[0] == "код":
                                    textop[0] = "кот"
                                textic_2 = " ".join(textop)
                                textic = str(textic_2).lower()
                                voice = True
                                using = True
                                if textic_2 != "":
                                    Output("Detected voice message!\nContents: " + textic_2)
                                del textop
                            del sound
                            del sample_audio
                    except:
                        textic_2 = ""
                        textic = ""
                        voice = False
                        using = False
                else:
                    textic_2 = event.object['text']
                    textic = event.object['text'].lower()
                    voice = False
                useprefix = False
                if event.from_chat:
                    chat_id = event.chat_id
                if textic.startswith(ReadFF("mention.txt")) and event.from_chat:
                    textic = textic[len(ReadFF("mention.txt"))]
                    textic_2 = textic_2[len(ReadFF("mention.txt"))]
                    useprefix = True
                if textic.startswith('/'):
                    textic = textic[1:]
                    textic_2 = textic_2[1:]
                    useprefix = True
                    using = True
                if event.from_user:
                    useprefix = True
                cmd = textic.split(' ')[0]
                parameter = textic_2.split(' ')[1:]
                flags = []
                for word in parameter:
                    if word.startswith("-") and word != "-":
                        flags.append(word.lower())
                        parameter.remove(word)
                parameter = ' '.join(parameter)

                #
                # Форс-снятие с троллинга
                #

                if textic == "forcetroll" and str(user_id) in admins and str(user_id) in trolling.keys():
                    del trolling[str(user_id)]
                    updatetroll()
                
                if textic == "forcemute" and str(user_id) in admins and str(user_id) in muted.keys():
                    del muted[str(user_id)]
                    updatemuted()

                if cmd in commands: #and (not "#hide" in ReadFF(COMMANDSDIR + cmd) or user_id in admins):
                    using = True
                    InfoMsg("Обработка...")
                if textic_2 == "":
                    using = False

                coun = 0
                for x in rcs:
                    coun += 1
                    try:
                        procmsg("Starting CoreRC module - " + str(coun))
                        exec(x)
                        succ()
                    except Exception as e:
                        failcomplete()
                        exc_type, exc_value, exc_tb = sys.exc_info()
                        messagecust('Proccess died: \n' + "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)), 242722587)
                        system_errors += "Unable to start coreRC module - " + str(e) + endl

                if using == True and user_id in banned:
                    using = False

                if using == True and str(user_id) in trolling.keys():
                    using = False

                using = using and permitting_()

                #
                # Обработчик-оптимизатор команд. Кусается!
                #
                if using:
                    try:
                        replytext = event.object["reply_message"]["text"]
                        if parameter == "":
                            parameter = replytext
                            InfoMsg("Detected reply to message")
                    except:
                        pass
                    try:
                        writeTo(detectfull(event.object['attachments'][0]), 'argv_picture.txt')
                    except:
                        writeTo("none", "argv_picture.txt")
                    ins = 'false'

                    #Проверка в командах
                    for x in commands:
                        if cmd == x and useprefix:
                            vk.messages.setActivity(type="typing", peer_id=peer_id)
                            if getparam(user_id, "stage") == "default":# and " | " not in textic_2:
                                Output(f"""
=================================
Detected command - {x}!
Syntax: {textic_2}
Parameter: {parameter}
""")
                                InfoMsg("Executing command - " + x)
                                ins = 'true'
                                an = 1
                                if modes[commands.index(x)] == "pic" and ReadFF("argv_picture.txt") == "none":
                                    message("Команда требует прикрепленного изображения.")
                                    an = 0
                                if modes[commands.index(x)] == "start" and parameter == "":
                                    message("Команда требует аргумента.\n\nПример использования: " + cmd + " текст")
                                    an = 0
                                code_js = convertjson(ReadFF(f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.json"))
                                author = code_js["author"]
                                mode = code_js["mode"]
                                identificator = code_js["identificator"]
                                command_ru = code_js["command_ru"]
                                description = code_js["description"]
                                if an == 1:
                                    if not code_js["restricted"]:
                                        try:
                                            code = ReadFF(f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.py")
                                            procmsg("Command starting...")
                                            if not code_js["testing"]:
                                                exec(code)
                                                PlusWrite("used command: " + ids[commands.index(x)] + ".py\n", "commandslog.txt")
                                                try:
                                                    sc = int(getparam(user_id, "score"))
                                                    sc = sc + 1
                                                    setparam(user_id, "score", str(sc))
                                                except:
                                                    Output("CUMv2/Warning: unable to +1 in user's score")
                                                    pass
                                                succ()
                                            else:
                                                if isTester(user_id):
                                                    exec(code)
                                                else:
                                                    message("Вы не являетесь тестировщиком, если вы хотите стать тестировщиком, то обратитесь в @catpy.beta!", reply=True)
                                        except vk_api.exceptions.ApiError as e:
                                            if str(e).startswith("[917]"):
                                                message("Упс! Я не могу выполнить эту команду, потому что не являюсь админом этого чата! Назначьте меня админом и повторите попытку снова.")
                                        except Exception as e:
                                            Output(e)
                                            message(f"Команда {command_ru} [{identificator}] аварийно завершилась из-за ошибки.\nКод ошибки: {generrorcode(str(e), identificator)}\nАвтор команды: {author}\nИнформация об ошибке была автоматически отправлена администрации бота.")
                                            exc_type, exc_value, exc_tb = sys.exc_info()
                                            mta(f"==CatABMS-Package BugReport==\nОбщая информация:\n\nСерверное время: {readableDate(time.time())}\nКоманда: {command_ru} [{identificator}]\nАвтор команды: {author}\nПользователь: {getmention(user_id)} ({user_id})\nID диалога (peer_id): {peer_id}\nПереданный параметр: {parameter}\nКод ошибки: {e}\n\nTraceback ошибки:\n\n" + '\n'.join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                                            Output("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                                            failcomplete()
                                    else:
                                        if str(user_id) not in ReadFF("usr/restricted.txt").split(","):
                                            message("Данная команда внесена в пакет потенциально оскорбительных команд. Однако, подключить пакет можно командой \"подключить-пакет\".")
                                        else:
                                            try:
                                                code = ReadFF(f"{COMMANDSDIR}{ids[commands.index(x)]}/{ids[commands.index(x)]}.py")
                                                if not code_js["testing"]:
                                                    exec(code)
                                                else:
                                                    if isTester(user_id):
                                                        exec(code)
                                                    else:
                                                        message("Вы не являетесь тестировщиком, если вы хотите стать тестировщиком, то обратитесь в @catpy.beta!", reply=True)
                                            except Exception as e:
                                                failcomplete()
                                                Output(e)
                                                message("Команда " + command_ru + " [" + identificator + f"] аварийно завершилась из-за ошибки.\nКод ошибки: {generrorcode(str(e), identificator)}\nАвтор команды: " + author + "\nИнформация об ошибке была автоматически отправлена администрации бота.")
                                                exc_type, exc_value, exc_tb = sys.exc_info()
                                                mta("==CatABMS-Package BugReport==\nОбщая информация:\n\nСерверное время: " + readableDate(time.time()) + "\nКоманда: " + command_ru + " [" + identificator + "]\nАвтор команды: " + author + "\nПользователь: " + getmention(user_id) + " (" + str(user_id) + ")\nID диалога (peer_id): " + str(peer_id) + "\nПереданный параметр: " + parameter + "\nКод ошибки: " + str(e) + "\n\nTraceback ошибки:\n\n" + "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                                                Output("\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
                                                #failcomplete()
                                            except vk_api.exceptions.ApiError as e:
                                                if str(e).startswith("[917]"):
                                                    message("Упс! Я не могу выполнить эту команду, потому что не являюсь админом этого чата! Назначьте меня админом и повторите попытку снова.")
                                Output("=================================\n\n")
                            """ else:
                                try:
                                    outputd = True
                                    firstpart = textic.split(" | ")
                                    cmd1 = firstpart[0].split(' ')[0]
                                    parameter = " ".join(firstpart[0].split(' ')[1:])
                                    exec(ReadFF(f"{COMMANDSDIR}{ids[commands.index(cmd1)]}/{ids[commands.index(cmd1)]}.py"))
                                    parameter = " ".join(firstpart[1].split(" ")[1:]) + " " + ReadFF("usr/lastoutput.txt")
                                    outputd = False
                                    exec(ReadFF(f"{COMMANDSDIR}{ids[commands.index(firstpart[1].split(' ')[0])]}/{ids[commands.index(firstpart[1].split(' ')[0])]}.py"))
                                except Exception as e:
                                    message(f"Ошибка при запуске пайпов: {str(e)}")
                                try:
                                    exec(ReadFF(f"chains/{getparam(user_id, 'stage')}.py"))
                                except Exception as e:
                                    setparam(user_id, "stage", "default")
                                    mta("catABMS chains: error: " + str(e)) """

                #elif not using and textic_2 != "" and useprefix and str(user_id) in ReadFF("usr/restricted.txt").split(",") and user_id not in banned and str(user_id) not in trolling.keys() and user_id not in muted and permitting_():
                #    try:
                #        try:
                #            anss = str(Get("http://artificalintellect.pythonanywhere.com/gen?text=" + textic_2))
                #            if anss.startswith("error") or anss == "0":
                #                message("Упс, а я пока не знаю, как на это ответить!")
                #            else:
                #                #
                #                # "Возможно, вы имели ввиду?"
                #                #
                #                g = []
                #                for j in commands:
                #                    if Similar(cmd, j):
                #                        g.append(j)
                #                seems_txt = ""
                #                if g != []:
                #                    for h in g:
                #                        seems_txt += "\n -> " + h
                #                    message("Возможно, вы имели ввиду: \n" + seems_txt)
                #                else:
                #                    message(anss.replace("%USERNAME", getname(user_id)))
                #        except:
                #            pass
                #    except:
                #        pass
                elif getparam(user_id, "stage") != "default" and event.from_user:
                    try:
                        exec(ReadFF(f"chains/{getparam(user_id, 'stage')}.py"))
                    except Exception as e:
                        message("Модуль цепочки " + getparam(user_id, "stage") + " крашнулся с ошибкой: " + str(e) + ". Ошибка была отправлена администрации бота.")
                        setparam(user_id, "stage", "default")
                if getparam(user_id, "stage") != "default" and event.from_user and textic == ".exit":
                    message("Выход из модуля цепочки...")
                    setparam(user_id, "stage", "default")
                    message("Успешно.")
                elif user_id in banned and useprefix == True:
                    message("Вы были заблокированы администрацией catpy.")
                elif str(user_id) in trolling.keys() and useprefix == True:
                    message(trolling[str(user_id)])
                else:
                    InfoMsg("Request will be ignored due to optimization.")

            if event.type == VkBotEventType.GROUP_LEAVE:
                Output(f"""
=================================
-1 subscriber: {getname(event.object['user_id'])} ({event.object['user_id']})
=================================
""")
                sexmessage('Я всё вижу! Не мог бы ты сообщить нам командой "репорт", почему ты отписался, нам важно это знать!', 'Не могла бы ты сообщить нам командой "репорт", почему ты отписался, нам важно это знать!', event.object['user_id'])
                mta('🔻Отписался: ' + getmention(event.object['user_id']))

            if event.type == VkBotEventType.GROUP_JOIN:
                Output(f"""
=================================
+1 subscriber: {getname(event.object['user_id'])} ({event.object['user_id']})
=================================
""")
                messagecust('Cпасибо за подписку!', event.object['user_id'])
                mta('🔺Подписался: ' + getmention(event.object['user_id']))

            if event.type == VkBotEventType.MESSAGE_REPLY:
            #    setparam("sent", getparam("surrogate", "sent") + len(textic_2), "surrogate")
                try:
                    peer_id = event.object['peer_id']
                    text = event.object['text']
                    if peer_id > 2000000000:
                        Output(f"""
=================================
Message sent to conversation: {peer_id}\nText: {text}
=================================
""")
                    else:
                        Output(f"""
=================================
Message sent to user: {getname(peer_id)} ({peer_id})\nText: {text}
=================================
""")
                except: pass

            if event.type == VkBotEventType.WALL_POST_NEW:
                Output(f"""
=================================
New post: wall{event.object["owner_id"]}_{event.object["id"]}
=================================
""")
                messagecust("Хей, юзеры! У меня на стене новый пост!", 2000000299, attachment="wall{}_{}".format(event.object["owner_id"], event.object["id"]))
            if int(psutil.virtual_memory().percent) >= 90:
                mta(f"ПЕРЕМОГА БЛЯДЬ! ЗАНЯТО {psutil.virtual_memory().percent}% ОЗУ!!")
            new_list = dir()
            diff = list(set(new_list) - set(old_list))
            Output("Catware Memory Gun: u should clean this variables: " + ", ".join(diff))
            if enable_memgun_cleaning:
                for kef in diff:
                    exec(f"del {kef}")
    except Exception as e:
        InfoMsg("Hardened Core is working: main cycle crashed due to " + str(e) + ": " + str(__name__))
        exc_type, exc_value, exc_tb = sys.exc_info()
        mta(f"Ядро успещьно рухнуло!!1!! Трейс:\n" + '\n'.join(traceback.format_exception(exc_type, exc_value, exc_tb)))
