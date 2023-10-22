# CatOS-Type Package
author = "catwared, aGrIk"
mode = "="
deps = 'None'
identificator = 'news'
command_ru = 'новости'
description = 'Свежие новости'

obj = RSSParse(Get("https://lenta.ru/rss/last24"))
nws_ = []
for iter in obj:
    nws_.append(iter["title"] + "\nПодробнее: " + ShortUrl(iter["link"]) + "\n\n")
message("Наиболее важные новости по данным Lenta.ru: \n" + "\n".join(nws_), reply=True)
