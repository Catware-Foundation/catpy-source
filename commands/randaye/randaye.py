# CatOS-type package
author = "catweird, aGrIk"
mode = "="
deps = 'None'
identificator = 'randaye'
command_ru = 'ауе'
description = 'секретная команда епта'
#hide

list_pril = "анальный,тупой,злой,добрый,быстрый,медленный,".split(",")
list_sus = "макщ,наркотик,носок,гей,либерал,школьник,навальный,пыня,зига,жириновский,разраб котопая,юра,стас,снюс,котопай,".split(",")

list_sush = "патроны,презервативы,сиги,сигареты,снюсик,деньги,кокс,наркотики,чай,табак,магнитофон,чифир,минет,пистолет,пулемёт,пистолет-пулемёт,отсос,стояк,говно,".split(",")
list_men = "деда,бати,мамы,папы,матери,сына,дедушки,бабушки,брата,сестры,племянника,дяди,путина,навального,котопая".split(",")

list_actions = "спиздил,продал,украл,взял,купил,одел".split(",")

message(f"{randd.choice(list_pril)} {randd.choice(list_sus)} {randd.choice(list_actions)} {randd.choice(list_sush)} {randd.choice(list_men)}", reply=True)

if randd.randint(1, 100) == 10: message("юра гей)", reply=True)

del list_pril
del list_sus
del list_sush
del list_men
del list_actions
