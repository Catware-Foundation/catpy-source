cont = False
if textic_2 not in categories:
    message("Категории <<" + textic_2 + ">> нет в списке. Попробуйте снова или напишите .exit для выхода из программы.")
else:
    message("Ставлю фокус на категорию " + textic_2 + ".")
    cont = True
    setparam(user_id, "appdata/FOD-category", textic_2)

if cont:
    message("Идёт поиск слова...")
    wrd = getword(textic_2)
    smiley = randd.choice(emoji_list)
    #message(wrd)
    message(f"""Внимание, игра начинается!
ТЕМА: {wrd['description']}
Длина: {str(len(wrd['word']))}
Категория: {wrd['category']}
Буквы - {wrd['wordlanguage']} язык

Слово - [{displayword(wrd, [], smiley)}]

Называйте букву. Для выхода из игры введите <<.exit>> без кавычек""")
    setparam(user_id, "appdata/FOD-word", wrd)
    setparam(user_id, "appdata/FOD-word-letters", ",".join(wrd['letters']))
    setparam(user_id, "appdata/FOD-word-letters-solved", "")
    setparam(user_id, "appdata/FOD-smiley", smiley)
    setparam(user_id, "stage", "fod2")
