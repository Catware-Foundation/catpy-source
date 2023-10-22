exec(ReadFF("lib/transliterate.py"))
nick = transliterate(parameter.lower().replace(" ", "_")).replace("i", "1").replace("o", "0").replace("t", "7").replace("e", "3").replace("l", "1")
ayesex = randd.choice([1, 2])
if ayesex == 1:
    nick = nick.replace("ch", "4")
else:
    nick = nick.replace("a", "4")

message(nick)
