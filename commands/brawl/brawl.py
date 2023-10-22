я н# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'brawl'
command_ru = 'бравл'
description = 'Статистика игрока Brawl Stars по тэгу'

if not parameter.startswith("#"): parameter = "%23" + parameter
parameter = parameter.replace("#", "%23")

req = requests.get("https://api.brawlstars.com/v1/players/" + parameter, headers={"authorization": "Bearer медведер_блять_ахуительно_огромный_токен_от_бравл_старс"})

if req.status_code == 200:
    reqjs = req.json()
    message(f"""
Информация об игроке:

Ник: {reqjs["name"]}
Тег: {reqjs["tag"]}
Уровень: {reqjs["expLevel"]}
Трофеев: {reqjs["trophies"]}
Максимум трофеев: {reqjs["highestTrophies"]}

Побед 3 на 3: {reqjs["3vs3Victories"]}
Побед 2 на 2: {reqjs["duoVictories"]}
Одиночных побед: {reqjs["soloVictories"]}

""", reply=True)
elif req.status_code == 503:
    message("На сервере Brawl Stars временно проводятся технические работы, информация недоступна.", reply=True)
elif req.status_code == 429:
    message("Ошибка на стороне сервера Brawl Stars, информация недоступна.", reply=True)
    mta("Команда \"бравл\": превышен лимит запросов по токену API (429 HTTP). Информация от сервера: " + req.text)
elif req.status_code == 403:
    message("Ошибка на стороне сервера Brawl Stars, информация недоступна.", reply=True)
    mta("Команда \"бравл\": токен потерял доступ к API (403 HTTP). Информация от сервера: " + req.text)
else:
    message("Информация об игроке не найдена. Проверьте, верно ли вы ввели тег игрока.", reply=True)
