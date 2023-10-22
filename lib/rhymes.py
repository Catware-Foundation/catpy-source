
#
# Rhymes generator (rifme.net parser)
# ! REQUIRES SMARTGET LIBRARY !
# Catware, 2020
#

#headers = {'User-Agent': ua.random}
#def sget(URL):
#    return requests.get(URL, headers=headers).text

exec(ReadFF("lib/smartget.py"))

h = html2text.HTML2Text()
h.ignore_links = True
rhymes = []

def rhyme(textd):
    htext = h.handle(sget("https://rifme.net/r/" + str(textd) + "/0"))
    rhm = False
    for r in htext.split("\n"):
        if "## Наиболее точные рифмы для" in r:
            rhm = True
        if rhm:
            if "*" in r:
                rhymes.append(r[4:])
    return rhymes
