# CatOS-Type Package
author = "CatWeird, aGrIk"
mode = "="
deps = 'None'
identificator = 'death'
command_ru = 'смерть'
description = 'Предугадывание причины смерти. Можно указать число генерируемых смертей.'
#сука говно сперма хуй ублюдок! говно говно

glagols = "Убит,Изнасилован,Обоссан,Трахнут,Утоплен,Застрелен,Заражен,Отэлектризован,Задушен,Зарезан,Уничтожен,Замочен,Раздавлен,Оглушен,Захлебнёшься,Расстрелян,Зажарен,Зарезан,Застрелен,Ограблен,Сожжён,Отравлен,Сломан,Накормлен,Вкинут,Разрезан".split(",")
items = "тряпочкой,коронавирусом,сексом,сиськами,бабами,одноклассниками,одноклассницами,соседями,сигаретами,ножами,самолётом,снюсом,членом,спермой,водой,путиным,разрабом котопая,детьми,гомосеками,лесбиянками,маньяками,утюгом,тишиной,темнотой,хентаем,скайнетом,свиньями,мамкой,батей,братом,сестрой,преподом,домашкой,вейпом,виндой,лампой,говном,испаром,картоном,полкой,об асфальт".split(",")
time_glagol = "стирки,печати,нарезки,дрочки,оглушения,убийства,изнасилования,заражения,зарядки,удушения,уничтожения,избавления от,компилирования,оглушения,сна,мочеиспускания,суицида,избиения,покупки,продажи,настройки,конфигурации,установки,удаления,прослушивания,записи".split(",")
time_items = "бумаг,колбасы,тряпок,коронавируса,секса,одноклассниц,одноклассников,соседей,сигарет,ножа,самолёта,снюса,члена,спермы,путина,разраба котопая,детей,утюга,девок,твоей мамки,пидорасов".split(",")
help_items = "экрана,компьютера,анала,говна,метлы,тёлки,верёвок".split(",")

gachi_glagols = "Откулачен,Оттрахан,Изнасилован,Выебан".split(",")
gachi_items = "Dungeon Master'ом,парнем из следующей двери,Slave'ами,Leathermen'ом".split(",")
gachi_time_glagol = "фистинга,sucktion,spanking".split(",")
gachi_time_items = "fucking slaves,Dungeon Master'a,Leathermen'a,Boy next door'a,Billy Herrington".split(",")
gachi_help_items = "члена,кулака,slaves".split(",")

if parameter == "":
    message(randd.choice(glagols) + " " + randd.choice(items) + " во время " + randd.choice(time_glagol) + " " + randd.choice(time_items) + " с помощью " + randd.choice(help_items), reply=True)

try:
    p = int(parameter)
    gay = True
except:
    gay = False

if parameter == "-варианты":
    message("Доступно вариантов смерти: " + str(len(glagols) * len(items) * len(time_glagol) * len(time_items) * len(help_items)), reply=True)

if parameter == "-gachi":
    message(f"{randd.choice(gachi_glagols)} {randd.choice(gachi_items)} во время {randd.choice(gachi_time_glagol)} {randd.choice(gachi_time_items)} с помощью {randd.choice(gachi_help_items)}", reply=True)

if gay == True:
    try:
        deaths = []
        for sex in range(int(parameter)):
            deaths.append(randd.choice(glagols) + " " + randd.choice(items) + " во время " + randd.choice(time_glagol) + " " + randd.choice(time_items) + " с помощью " + randd.choice(help_items), reply=True)
        message("Причины:\n" + "\n\n".join(deaths), reply=True)
    except:
        message("Указано неверное число", reply=True)
