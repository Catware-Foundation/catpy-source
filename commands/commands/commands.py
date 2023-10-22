# CatOS-Type Package
author = "aGrIk, catwared"
mode = "="
deps = 'None'
identificator = 'commands'
command_ru = 'команды'
description = 'Список команд бота.\nИспользование: команды (флаг)\nФлаги:\n-откл, -доп, -лист'

#if "-откл" in flags:
#    message(ReadFF("disable_commands.txt"))
if "-доп" in flags:
    message(ReadFF("restricted_commands.txt"), reply=True)
elif "-лист" in flags:
    message(ReadFF("default_commands.txt"), reply=True)
else:
    message("📖 Команды catpy: https://ctw.re/commands.html\n\nТекстовая версия списка команд: команды -лист\nДополнительный пакет команд: команды -доп\n", 0, reply=True)
