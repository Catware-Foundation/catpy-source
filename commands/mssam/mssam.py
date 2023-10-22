##allowed_chars = list("qwertyuiopasdfghjklzxcvbnmQWEASDZXCRTYFGHVBNUIOJKLMP ")
##
##newparameter = ""
##for ch in parameter:
##    if ch in allowed_chars:
##        newparameter += ch
##    else:
##        pass
##parameter = newparameter
##
##if len(parameter) > 0:
##    try:
##        url = f"https://tetyys.com/SAPI4/SAPI4?text={parameter}&voice=Sam&pitch=100&speed=100"
##        Download(url, "tmp/mssam.wav")
##        sound = AudioSegment.from_wav("tmp/mssam.wav")
##        sound.export("tmp/mssam.ogg", format="ogg")
##        Voice("tmp/mssam.wav")
##    except Exception as e:
##        errr = requests.post("https://dpaste.com/api/v2/", data={"content": str(e), "title": "CatABMS / Microsoft Sam API Error"}).text
##        if str(errr) != "[901] Can't send messages for users without permission":
##            message(f"Не удалось озвучить текст. Сведения об ошибке -> {errr}")
##        else:
##            message("Я не могу отправлять тебе вложения, начни диалог со мной, и желательно подпишись.")
##else:
##    message("Указан пустой параметр. Вероятно, вы пытаетесь ввести что то не на английском языке.")
##
#
#Output("File «commands/mssam/mssam.py» is disabled by exf/disablefile.py. Hi from Catware👋🏻")

Output("File «commands/mssam/mssam.py» is disabled by exf/disablefile.py. Hi from Catware👋🏻")