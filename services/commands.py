
#listd = []
#hide_listd = []
#restricted_listd = []
#testing_listd = []
#disable_listd = []

#for x in os.listdir("commands"):
#    exec("\n".join(ReadFF("commands/" + x).split("\n")[:7]))
#    type_ = "default"
#    if "#disable" in ReadFF("commands/" + x):
#        type_ = "disable"
#    if "#hide" in ReadFF("commands/" + x):
#        type_ = "hide"
#    if "#restricted" in ReadFF("commands/" + x):
#        type_ = "restricted"
#    if "#testing" in ReadFF("commands/" + x):
#        type_ = "testing"

#    if type_ == "default":
#        listd.append(command_ru + ": " + description)
#    if type_ == "disable":
#        disable_listd.append(command_ru + ": " + description)
#    if type_ == "hide":
#        hide_listd.append(command_ru + ": " + description)
#    if type_ == "restricted":
#        restricted_listd.append(command_ru + ": " + description)
#    if type_ == "testing":
#        testing_listd.append(command_ru + ": " + description)

#writeTo("Команды бота\n\n" + "\n\n".join(listd), "default_commands.txt")
#writeTo("Отключённые команды бота\n\n" + "\n\n".join(disable_listd), "disable_commands.txt")
#writeTo("Скрытые команды бота\n\n" + "\n\n".join(hide_listd), "hidden_commands.txt")
#writeTo("Дополнительные команды бота\n\n" + "\n\n".join(restricted_listd), "restricted_commands.txt")
#writeTo("Нестабильные команды бота\n\n" + "\n\n".join(testing_listd), "testing_commands.txt")


listd = []
hide_listd = []
restricted_listd = []
testing_listd = []
disable_listd = []
htmlcode = ""

HTML_START = ReadFF("usr/startofhtml.txt").replace("$botname", botname).replace("$commands_count", str(len(os.listdir("commands"))))
CARD_TEMPLATE = ReadFF("usr/cardtemplate.txt")
HTML_END = ReadFF("usr/endofhtml.txt").replace("$botname", botname).replace("$commands_count", str(len(os.listdir("commands")))).replace("$catabms_version", version).replace("$codename", codename).replace("$releasedate", releasedate)

htmlcode += HTML_START
cards = []

for x in os.listdir("commands"):
    cmdjs = convertjson(ReadFF(f"{COMMANDSDIR}/{x}/{x}.json"))
    command_ru = cmdjs["command_ru"]
    description = cmdjs["description"]
    type_ = "default"
    if cmdjs["disabled"]:
        type_ = "disable"
    if cmdjs["hide"]:
        type_ = "hide"
    if cmdjs["restricted"]:
        type_ = "restricted"
    if cmdjs["testing"]:
        type_ = "testing"

    if type_ == "default":
        listd.append(cmdjs['command_ru'] + ": " + cmdjs['description'])
        card = CARD_TEMPLATE.replace("$commandname", cmdjs['command_ru']).replace("$description", description).replace("$author", cmdjs['author'])
        if card not in cards:
            htmlcode += card
            cards.append(card)
        else:
            pass
    if type_ == "disable":
        disable_listd.append(command_ru + ": " + description)
    if type_ == "hide":
        hide_listd.append(command_ru + ": " + description)
    if type_ == "restricted":
        restricted_listd.append(command_ru + ": " + description)
    if type_ == "testing":
        testing_listd.append(command_ru + ": " + description)

htmlcode += HTML_END

try:
    writeTo(htmlcode, "/home/catpy/server/commands.html")
except:
    pass

writeTo("Команды бота\n\n" + "\n\n".join(listd), "default_commands.txt")
writeTo("Отключённые команды бота\n\n" + "\n\n".join(disable_listd), "disable_commands.txt")
writeTo("Скрытые команды бота\n\n" + "\n\n".join(hide_listd), "hidden_commands.txt")
writeTo("Дополнительные команды бота\n\n" + "\n\n".join(restricted_listd), "restricted_commands.txt")
writeTo("Нестабильные команды бота\n\n" + "\n\n".join(testing_listd), "testing_commands.txt")
del HTML_START
del CARD_TEMPLATE
del cards
del htmlcode
del HTML_END
