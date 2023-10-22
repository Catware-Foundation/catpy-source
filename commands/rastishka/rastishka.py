# CatOS-Type Package
author = "CatWeird"
mode = "pic"
deps = 'None'
identificator = 'rastishka'
command_ru = 'кумыс'
description = 'Напаивает фотографию кумысом'

picture_url = ReadFF("argv_picture.txt")
Download(picture_url, "picture.jpg")
resize_image("picture.jpg", "handled_picture.jpg", (RandomInt(500, 1500), RandomInt(500, 1500)))
picturedata("handled_picture.jpg", "Картинка готова.")
