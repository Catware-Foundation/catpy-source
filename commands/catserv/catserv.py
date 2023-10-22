URL = "https://mcapi.ctw.re/v1/server"

try:
    info = json.loads(Get(URL))
    message(f"""ℹ️Информация по {info['motd']}
ℹ️Основная информация - - - - - - - - - - -
ℹ️Статус сервера: 🟢️Онлайн
🛠️Реализация сервера: {info['name']}
🔹️Версия сервера: {info['version']} {info['bukkitVersion']}

✅️Здоровье сервера - - - - - - - - - - - -
ℹ️Ядер сервера: {info['health']['cpus']}
⌛️Аптайм сервера: {convertint(info['health']['uptime'])}
💾️Занято памяти: {dvn(info['health']['totalMemory'])}
💾Всего памяти: {dvn(info['health']['maxMemory'])}
💾Свободно памяти: {dvn(info['health']['freeMemory'])}

👥️Игроки - - - - - - - - - - - - - - - - -
👥️Всего: {info['onlinePlayers']}/{info['maxPlayers']}""")
except Exception as e:
    message(e)
