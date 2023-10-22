
def getans(txt):
    typicals = []
    global answers
    keyz = list(answers.keys())
    try:
        txt = txt.lower()
        return randd.choice(answers[txt])
    except Exception as e:
        return "error"