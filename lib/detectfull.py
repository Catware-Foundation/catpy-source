
#
# Catware Detecting Full Size Image for VK_API
#
# Спизженно из Catinka (чесно)
#
# Возвращает URL большей картинки
#
# Требует обьект изображения (["attachments"][picture_index])
#

def detectfull(pictureobject):
    maximum = 0
    result = ""
    for u in pictureobject["photo"]["sizes"]:
        if u["height"]*u["width"] > maximum:
            maximum = u["height"]*u["width"]
            result = u["url"]
    return result

def detectfullvid(videoobject):
    maximum = 0
    result = ""
    for u in videoobject["video"]["sizes"]:
        if u["height"]*u["width"] > maximum:
            maximum = u["height"]*u["width"]
            result = u["url"]
    return result
