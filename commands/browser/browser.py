# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'browser'
command_ru = 'браузер'
description = 'Получает текст веб-страницы'
h = html2text.HTML2Text()

#disable

if not parameter.startswith("http"): parameter = "http://" + parameter

if "-links" not in parameter:
    h.ignore_links = True
else:
    parameter = parameter.replace("-links", "").replace("  ", " ")

try:
    message("Получение текста...")
    text = h.handle(str(Get(parameter)))
    if "None" not in text:
        message(text)
    else:
        message("Текст получен, но он ничего не содержит.\n\nВозможно, это вызвано тем, что у бота неполный доступ в интернет.", reply=True)
except Exception as e:
    message("Ошибка. ", reply=True)
