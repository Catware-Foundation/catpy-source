# CatOS-Type Package
author = "Hornet"
mode = "start"
deps = 'None'
identificator = 'hi_to_admin'
command_ru = 'приветадминам'
description = 'Передает привет админам котопая от юзера'

if user_id not in reportbanned:
    mta('Хей, админы, вам салютует ' + getmention(user_id) + ' (' + str(user_id) + ')! Вот, что он просил передать: ' + parameter)
    message("Привет передан!", reply=True)
else:
    message("Вам заблокирована возможность репорта.", reply=True)
