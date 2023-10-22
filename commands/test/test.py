#CatOS-type package
author = "catwared"
mode = "="
deps = 'None'
identificator = 'test'
command_ru = 'тест'
description = 'Тестовая команда'

if prevention_mode == True:
    prevent = f"⚠{botname} находится в режиме профилактики и может не отвечать/выдавать глюки в особых местах"
else:
    prevent = ""

if only_admins:
    addition = "Бот запущен в безопасном режиме."
else:
    addition = ""

message(f"""Тест успешен!
Время работы бота: {convertint(time.time() - float(ReadFF('start-time.txt')))}
Серверное время: {readableDate(time.time())}
Скорость обработки: {time.time() - start}
Занято ОЗУ: {str(psutil.virtual_memory().percent)}%
Примерная скорость операций в секунду на сервере: {dvn(serverspeed)}/s

Целостность: {int(100 - percent(systemcare, careless))}%
О целостности можно узнать по ссылке - https://vk.com/@catpy-celostnost-kotopaya-v-detalyah

{prevent}

{addition}

Не работает команда? Обнаружили ошибку? Сообщите нам при помощи команды "/репорт"!
""", reply=True)
