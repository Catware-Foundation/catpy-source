for x in os.listdir("commands"):
    cmd = ReadFF(f"commands/{x}/{x}.py")
    js = loads(ReadFF(f"commands/{x}/{x}.json"))
    if "#testing" in cmd:
        js["testing"] = True
    else:
        js["testing"] = False
    if "#hide" in cmd:
        js["hide"] = True
    else:
        js["hide"] = False
    if "#restricted" in cmd:
        js["restricted"] = True
    else:
        js["restricted"] = False
    if "#disable" in cmd:
        js["disabled"] = True
    else:
        js["disabled"] = False
    writeTo(dumps(js, ensure_ascii=False), f"commands/{x}/{x}.json")
