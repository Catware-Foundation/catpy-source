wrdss = parameter.split(' ')
fl = []
for k in wrdss:
    fl.append(k[0])
randd.shuffle(fl)
nfl = []
cont = 0
for wef in wrdss:
    nfl.append(fl[cont] + wef[1:])
    cont += 1

message(" ".join(nfl))
