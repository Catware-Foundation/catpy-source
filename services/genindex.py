#genindex = ReadFF("usr/indexhtml").replace("$botname", botname).replace("$advice", "Наш труд - ваше удобство использования.").replace("$command1", "перелом").replace("$comand1descr", "Сломать фотографию. (требует приложенной фотки)").replace("$command2", "вики").replace("$comand2descr", "Поиск по википедии. Требует аргумента к команде").replace("$command3", "демотиватор").replace("$comand3descr", "Создание демотиваторов.<br>Использование: демотиватор текст сверху;текст снизу").replace("$command4", "скачатьаудио").replace("$comand4descr", "Скачивание аудиозаписей ВКонтакте (требует приложенной аудиозаписи)").replace("$command5", "зальго").replace("$comand5descr","Превращение текста в ZALGO (Убедительная просьба не срать этим в беседы!")
#writeTo(genindex, "/home/catpy/server/index.html")