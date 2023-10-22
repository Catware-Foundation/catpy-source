uscom = 0
for aye in os.listdir("users"): 
    try:
        uscom += int(getparam(aye, "score"))
    except:
        pass
message(uscom)