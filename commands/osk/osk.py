# CatOS-Type Package
author = "catwared"
mode = "="
deps = 'None'
identificator = 'osk'
command_ru = 'оск'
description = 'Придумывает ПЕРЕПОЛНЯЮЩЕЕ НЕГАТИВОМ оскорбление. Используйте флаг -gachi для придумывания гачи-прозвища'


hohol_first = "швайно,свино,хрюне,сало,хохло,кибер,говно,гомо".split(",")
hohol_second = "пидор,хохол,хохлинка,чмо,урод,ебан,хуйло,свинья,педик".split(",")

gachi_first = "gachi,fucking ,cumming , leather,dungeon,spanking,gay,bondage".split(",")
gachi_second = "slave,master,men,gay,anal,semen,cum,website".split(",")

first_root = "писько,блядо,хуе,сучко,говно,хохло,швайно,жопо,кало,тупо,сопле,козло,криво,пидо,мудо,очко,грешно,гнидо,пердо,шлюхо,страшно,гнидо,косо,ебле".split(",")
pril = "блядый,страшный,вонный,жирный,ротый,ебливый,ссущий,ногий,вагинный,говный,кривой,хуий,сучкий,хохлый,швайный,жопый,калый,тупый,всратый,ауешный,пидрый".split(",")
sus2 = "глист,пидр,сран,дрист,ящер,хлыст,завр,звон,ящер,ёб,хуй,трах,бляд,жуй,срак".split(",")
prefix = "Гм,Так-с,Дай подумать,Та-ак,*Сонно смотрит на список участников BTS*,*Придумывает имя Байдену*,*Подгружает свой словарный запас*,*Открывает словарь русского языка*,Что, опять? Ну-с...,*Открывает словарь русского мата...*".split(",")
prefix2 = "Spanking,Cumming,Fisting".split(",")


cnt = 1

if "-c" in parameter:
    parameterd = parameter.split(" ")
    for aye in parameterd:
        if aye.startswith("-c"):
            try:
                cnt = int(aye[2:])
                parameter = parameter.replace(aye, "")
            except:
                message("Неправильно задано число. Устанавливаю значение на 1.", reply=True)
                cnt = 1

for ayayayyay in range(cnt):
    if parameter == "":
        message(randd.choice(prefix) + "...")
        message("Придумал: " + randd.choice(first_root) + randd.choice(pril) + " " + randd.choice(first_root) + randd.choice(sus2), reply=True)

    if "-gachi" in parameter:
        message("♂️" + randd.choice(prefix2) + "..." + "♂️")
        message("Придумал: " + randd.choice(gachi_first) + randd.choice(gachi_second), reply=True)

    if "-hohol" in parameter:
        message("卐卐卐️" + randd.choice(prefix2) + "..." + "卐卐卐️")
        message("Придумал: " + randd.choice(hohol_first) + randd.choice(hohol_second), reply=True)

#restricted
