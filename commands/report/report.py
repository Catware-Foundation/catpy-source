# CatOS-type package
author = "catweird, aGrIk"
mode = "start"
deps = 'None'
identificator = 'report'
command_ru = 'репорт'
description = 'Отправить сообщение администрации ' + botname + '. Также можно прикладывать скриншот к репорту'

if user_id not in reportbanned:
    exec(ReadFF("lib/remta.py")) # Импортирование инструкции reMTA.
    # Проверка наличия картинки в репорте
    if isTester(user_id):
        additional = "(тестировщик)"
    else:
        additional = ""
    if ReadFF("argv_picture.txt") != "none":
        mtapicture(ReadFF("argv_picture.txt"), f'Новый репорт\nЧат: {peer_id}\nОтправитель: {getmention(user_id)} {additional}\nТекст сообщения: {parameter}')
        message('Репорт успешно отправлен!', reply=True)
    # И если она не прикреплена
    else:
        mta(f'Новый репорт\nЧат: {peer_id}\nОтправитель: {getmention(user_id)} {additional}\nТекст сообщения: {parameter}')
        message('Репорт успешно отправлен', reply=True)
else:
    message("Вам заблокирована возможность репорта.", reply=True)
