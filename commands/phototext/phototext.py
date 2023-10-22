# CatOS-type package
author = 'aGrIk'
mode = 'pic'
deps = 'None'
identificator = 'phototext'
command_ru = 'фотовтекст'
description = 'Распознаёт текст на фото и выводит его'

try:
    #message("жывтоне!!! иду подгружать")
    Download(ReadFF("argv_picture.txt"), "usr/phototext.jpg")
    #message("жывтоне!!! иду интерпретировать")
    cfg = r"--oem 3 --psm 0"
    res = pytesseract.image_to_string(Image.open("usr/phototext.jpg"), lang='eng+rus', config=cfg)
    #message("жывтоне!!! иду удалять")
    os.remove("usr/phototext.jpg")
    if res:
        message("Результат: " + res)
    else: message("Не удалось распознать текст на картинке.")
except:
    message("Не удалось распознать текст на картинке.")
