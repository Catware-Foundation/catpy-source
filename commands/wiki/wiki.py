# CatOS-type package
author = "catwared, aGrIk"
mode = "start"
deps = 'None'
identificator = 'wiki'
command_ru = 'вики'
description = 'Поиск в Википедии\nИспользуйте флаг -кратко для сокращения информации в размер 4 предложений.'

if "-кратко" in flags:
    try:
        wiki_res = wikipedia.summary(parameter, sentences=4)
        if "Джордж Перри Флойд" not in wiki_res: message(wiki_res + "\nПодробнее: " + ShortUrl(wikipedia.page(parameter).url), reply=True)
        else: message("Аъаъаъаъааъъаъаа убили негра убили негра убили негра\nПодробнее: " + ShortUrl(wikipedia.page(parameter).url), reply=True)
    except wikipedia.exceptions.DisambiguationError as e:
        mr = '\n'.join(str(e).split('\n')[1:])
        message(f"Уточните, что вы имели ввиду:\n {mr}", reply=True)
    except Exception as e:
        message('Ничего не найдено. ' + str(e), reply=True)
else:
    try:
        wiki_res = wikipedia.summary(parameter)
        if "Джордж Перри Флойд" not in wiki_res: message(wikipedia.summary(parameter) + "\nПодробнее: " + ShortUrl(wikipedia.page(parameter).url), reply=True)
        else: message("Аъаъаъаъааъъаъаа убили негра убили негра убили негра\nПодробнее: " + ShortUrl(wikipedia.page(parameter).url), reply=True)
    except wikipedia.exceptions.DisambiguationError as e:
        mr = '\n'.join(str(e).split('\n')[1:])
        message(f"Уточните, что вы имели ввиду:\n {mr}", reply=True)
    except Exception as e:
        message('Ничего не найдено. ')
