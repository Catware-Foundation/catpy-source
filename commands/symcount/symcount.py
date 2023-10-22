# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'symcount'
command_ru = 'символ'
description = 'Считает встречаемость каждого символа в тексте'

symbs = list(parameter.replace("\n", "").lower())
symbs2 = []
symbs_ret = f"Всего символов: {len(symbs)}\nЧастота символов в тексте:\n"

for g in symbs:
    if g not in symbs2:
        symbs_ret += f'\n"{g}" - {round(percent(len(symbs), symbs.count(g)), 2)}% ({symbs.count(g)})'
        symbs2.append(g)

message(symbs_ret, reply=True)
del symbs_ret
del symbs2
del symbs
