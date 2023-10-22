# CatOS-type package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'searchpic'
command_ru = 'пикчи'
description = 'Поиск картинок (отдельное спасибо vk.com/opensnuse)'

message("так я тут")

"""
exec(ReadFF("lib/searchpictures.py"))
#disable
"""
searx = convertjson(Get(f"https://roughs.ru/api/search?q={parameter}&format=json&source_from=vk.com/catpy&categories=images&safesearch=1"))["results"]

message(searx)

'''
if len(searx) > 5:
    upload = VkUpload(vk_session)
    attchms = []
    chosen = []
    for aye in range(5):
        chosen.append(randd.choice(aye))
    for aye in chosen:
        image = session.get(aye["img_src"], stream=True)
        photo = upload.photo_messages(photos=image.raw)[0]
        attchms.append(f"photo{photo['owner_id']}_{photo['id']}")
    message(f"Картинки по запросу \"{parameter}\":", attachment=",".join(attchms), reply=True)
'''
