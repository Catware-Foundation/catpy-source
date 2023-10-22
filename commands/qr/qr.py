# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'qr'
command_ru = 'qr'
description = 'Сгенерировать qr код'

try:
    img = qrcode.make(parameter)
    img.save('usr/qr.png')

    picturedata("usr/qr.png", "Ваш QR код")
    del img
except:
    message("Не удалось сгенерировать QR код", reply=True)
