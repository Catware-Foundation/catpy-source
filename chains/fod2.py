ltr = textic[0]
wrd = convertjson(getparam(user_id, "appdata/FOD-word"))
ltrs = getparam(user_id, "appdata/FOD-word-letters").split(",")
sltrs = getparam(user_id, "appdata/FOD-word-letters-solved").split(",")
smiley = getparam(user_id, "appdata/FOD-smiley")
if list(set(ltrs) - set(sltrs)) != []:
    if ltr in ltrs:
        sltrs.append(ltr)
        if list(set(ltrs) - set(sltrs)) != []:
            message("Правильно!\n\n" + displayword(wrd, sltrs, smiley))
        else:
            message("Поздравляем, вы успешно разгадали слово - " + wrd['word'])
            setparam(user_id, "stage", "default")
    else:
        message("Такой буквы нет.\n\n" + displayword(wrd, sltrs, smiley))
else:
     message("Поздравляем, вы успешно разгадали слово!")
     setparam(user_id, "stage", "default")
setparam(user_id, "appdata/FOD-word-letters", ",".join(ltrs))
setparam(user_id, "appdata/FOD-word-letters-solved", ",".join(sltrs))

