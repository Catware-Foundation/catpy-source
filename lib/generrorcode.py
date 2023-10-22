exec(ReadFF("lib/transliterate.py"))
def generrorcode(text, id):
    id = transliterate(str(id))
    text = transliterate(str(text))
    osn = id + text
    osn = "".join("{:02x}".format(ord(c)) for c in osn)
    osn = osn.replace("_", "")
    if len(osn) < 20:
        return osn[:10]
    else:
        n = int(len(osn) / 10)
        res = [osn[i:i+n] for i in range(0, len(osn), n)]
        a = ''
        for x in res:
            try:
                a += x[res.index(x)]
            except:
                pass
        if len(a) < 10:
            a = a * 10
            a = a[:10]
        return a.lower()
