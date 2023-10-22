# CatOS-type package
author = "catwared"
mode = "pic"
deps = 'None'
identificator = 'animefind'
command_ru = 'чтозааниме'
description = 'Поиск аниме по приложенному изображению.'

message("Поиск...", reply=True)
a = Get("https://trace.moe/api/search?url=" + ReadFF("argv_picture.txt"))
message(a, reply=True)

#disable
