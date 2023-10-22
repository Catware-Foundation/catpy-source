ng = True
while ng:
    t = genshitpost()
    if t.replace(" ", "") == "":
        pass
    else:
        message(t)
        ng = False
