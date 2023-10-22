# CatOS-type package
author = 'aGrIk'
mode = 'start'
deps = 'None'
identificator = 'raskladka'
command_ru = 'раскладка'
description = 'Меняет раскладку текста'

#disable

smbs = ReadFF("smbs.txt").split("\n")
smbeng = smbs[0]
smbrus = smbs[1]

ret = list(parameter)


for x in range(len(ret)):
    if ret[x] in smbeng:
        ret[x] = smbrus[smbeng.index(ret[x])]
    elif ret[x] in smbrus:
        ret[x] = smbeng[smbrus.index(ret[x])]

message(f"Результат изменения раскладки:\n\n{''.join(ret)}", reply=True)
del smbs
del smbeng
del smbrus
del ret
