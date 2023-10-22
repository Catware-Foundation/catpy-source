# CatABMS-type executable
author = "AFaGP"
mode = "start"
deps = "None"
identificator = "rask"
command_ru = 'рас'
description = "Меняет раскладку с английской на русскую и наоборот\n\nИспользование: рас анг/рус текст для конвертации\n\nПример: рас рус rnj ghjxbbnfk njn utq"

charmap_ru = "ёйфячыцувсмакепитрнгоьблшщдюжэзхъ "
charmap_eng = "`qazxswedcvfrtgbnhyujm,kiol.;'p[] "

def rask_ru(x):
    msg1 = str(x).replace("`","ё").lower()
    msg1 = msg1.replace("q","й").replace("w","ц").replace(".","ю").replace(",","б").replace("m","ь").replace("n","т").replace("b","и").replace("v","м").replace("c","с").replace("x","ч").replace("z","я").replace("'","э").replace(";","ж").replace("l","д").replace("k","л").replace("j","о").replace("h","р").replace("g","п").replace("f","а").replace("d","в").replace("s","ы").replace("a","ф").replace("]","ъ").replace("[","х").replace("p","з").replace("o","щ").replace("i","ш").replace("u","г").replace("y","н").replace("t","е").replace("r","к").replace("e","у").replace("э ",", ").replace("/ ",". ").replace("? ",", ").replace("& ","? ").replace("&","?")
    return str(msg1)

def rask_ing(x):
    msg1 = str(x).replace("ё","`")
    msg1 = msg1.replace("й","q").replace("ц","w").replace("ю ",". ").replace("б ",", ").replace("ь","m").replace("т","n").replace("и","b").replace("м","v").replace("с","c").replace("ч","x").replace("я","z").replace("э ","' ").replace("ж ","; ").replace("д","l").replace("л","k").replace("о","j").replace("р","h").replace("п","g").replace("а","f").replace("в","d").replace("ы","s").replace("ф","a").replace("ъ ","] ").replace(" х"," [").replace("з","p").replace("щ","o").replace("ш","i").replace("г","u").replace("н","y").replace("е","t").replace("к","r").replace("у","e").replace(",","э").replace(".","/").replace(", ","? ").replace("? ","& ").replace("?","&")
    return str(msg1)

res = ''

for n in parameter:
    if n in charmap_ru:
         res += rask_ing(n)
    elif n in charmap_eng:
         res += rask_ru(n)
    else:
         res += n

message(res)
