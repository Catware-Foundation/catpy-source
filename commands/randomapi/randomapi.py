sources = {
"мемы": ["ukrmemes", "catdeb", "2sdp", "aye.catware"],
"обои": ["ipados_wallpapers", "win10_wallpapers", "macos_wallpapers", "vista_wallpapers"],
"майн": ["blocks", "items"]
}

if parameter == "":
    picture("https://randomapi.ctw.re/name=" + randd.choice(sources[randd.choice(["мемы", "обои", "майн"])]), "Случайное изображение:")

elif parameter != "лист" and parameter != "":
    if parameter not in sources.keys():
        message("Нет такого источника. Введите рандом лист для получения списка источников.")
    else:
        picture("https://randomapi.ctw.re/name=" + randd.choice(sources[parameter]), "Случайное изображение из источника <<" + parameter + ">>")

else:
    message("""Список доступных источников:
мемы - мемы из рандомных источников, среди которых паблики @catdeb, @aye.catware, @2sdpdl, и мемы из Украинского TikTok.
обои - обои рабочего стола из Windows 10, Vista, MacOS, IpadOS.
майн - случайный блок или предмет из Minecraft Java Edition.

Пример использования команды: рандом мемы""")
