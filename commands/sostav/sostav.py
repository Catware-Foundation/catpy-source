# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'sostav'
command_ru = 'состав'
description = 'Узнать состав какого либо продукта'


message("Запускаю узнаватель-состава1211...")
vlist = []

for s in parameter:
    s = s.lower()
    ve = ""
    if s == "й":
        ve = "йод"
    if s == "ц":
        ve = "цианид"
    if s == "у":
        ve = "уран"
    if s == "к":
        ve = "калий"
    if s == "е":
        ve = "емакс"
    if s == "н":
        ve = "натрий"
    if s == "г":
        ve = "гидрохлорит"
    if s == "ш":
        ve = "шиповник"
    if s == "з":
        ve = "зипрасидон"
    if s == "ф":
        ve = "фабомотизол"
    if s == "в":
        ve = "вакцина от коронавируса"
    if s == "а":
        ve = "алюминий"
    if s == "п":
        ve = "порнография"
    if s == "р":
        ve = "ржавчина"
    if s == "о":
        ve = "оксиген"
    if s == "л":
        ve = "литий"
    if s == "д":
        ve = "дилдо"
    if s == "ж":
        ve = "жидкость для вейпа"
    if s == "э":
        ve = "эбонит"
    if s == "я":
        ve = "яблочный сидр"
    if s == "ч":
        ve = "член макса"
    if s == "с":
        ve = "спирт"
    if s == "м":
        ve = "магнитофон"
    if s == "и":
        ve = "игорь"
    if s == "т":
        ve = "тротил"
    if s == "б":
        ve = "бор"
    if s == "ю":
        ve = "юбисофт"
    if s == "ъ":
        ve = "дорожный знак"
    if s == "ь":
        ve = "перья"
    if s == "щ":
        ve = "дерьмо"
    if s == ".":
        ve = "медь"
    if ve not in vlist:
        vlist.append(ve)
vlist = sorted(vlist)
for aye in range(vlist.count("")):
    vlist.remove("")
message(
"""В ходе экспертизы были выявлены следующие элементы химического состава:
""" + ", ".join(vlist), reply=True)
del vlist
del s
del ve
#restricted
