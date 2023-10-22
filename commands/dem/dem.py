# CatOS-type package
author = "catwared"
mode = "pic"
deps = 'None'
identificator = 'dem'
command_ru = 'дем'
description = 'Создание демотиваторов. Используйте ";" для разделения текста'
#hide
#disable
class Demotivator:
    pattern: Image
    background: Image
    MAX_LEN_BIG = 25
    MAX_LEN_SM = 40

    def __init__(self):
        self.pattern = Image.open('usr/demotivator.jpg')
        self.font1 = ImageFont.truetype(font="usr/demfont.ttf", size=48, encoding="unic")
        self.font2 = ImageFont.truetype(font="usr/demfont.ttf", size=28, encoding="unic")

    def create(self, url, text1, text2, name=None):
        if not name:
            name = str(randint(-32767, 32767)) + '.png'
        Download(url, "usr/download.jpg")
        img = Image.open("usr/download.jpg")
        img = img.resize((542, 358))
        result = self.pattern.copy()
        result.paste(img, (58, 58))

        def addBlack(num, img):
            self.background = Image.new('RGB', (img.size[0], img.size[1] + num * 50), (0, 0, 0))
            self.background.paste(img, (0, 0))
            return self.background.copy()

        # text1 = '\n'.join([textwrap.fill(x, self.MAX_LEN_BIG) for x in text1.split('\n')])
        # text2 = '\n'.join([textwrap.fill(x, self.MAX_LEN_SM) for x in text2.split('\n')])

        draw = ImageDraw.Draw(result)

        def formatText(text, font):
            text = text.split('\n').reverse() or [text]
            _l = len(text)
            for i in range(_l):
                while True:
                    w, h = draw.textsize(text[i], font=font)
                    if w < 630:
                        break
                    else:
                        splitted = text[i].split(' ')
                        if len(splitted) == 1:
                            break
                        if len(text) == i + 1:
                            text.append('')
                        text[i + 1] = f'{text[i + 1]} {splitted.pop(0)}'
                        text[i] = ' '.join(splitted)
            if _l == len(text):
                return '\n'.join(list(text.reverse() or text))
            else:
                return formatText('\n'.join(list(text.reverse() or text)), font)

        text1 = formatText(text1, self.font1).lstrip()
        text2 = formatText(text2, self.font2).lstrip()

        w1, h1 = draw.textsize(text1, font=self.font1)
        w2, h2 = draw.textsize(text2, font=self.font2)

        blackNum = 0
        if h1 + h2 > 140:
            blackNum += ceil((h1 + h2 - 140) / 50)
        result = addBlack(blackNum, result)
        del blackNum

        draw = ImageDraw.Draw(result)
        draw.multiline_text(((655 - w1) / 2, 450), text1, fill="white", font=self.font1, align="center")
        draw.multiline_text(((655 - w2) / 2, 470 + h1), text2, fill="white", font=self.font2, align="center")

        result.save("usr/demotivatord.png")

if parameter != "":
    try:
        p = parameter.split(";")
    except:
        p = [parameter, ""]
    d = Demotivator()
    d.create(ReadFF("argv_picture.txt"), p[0], p[1])
    picturedata("usr/demotivatord.png", "ваш\nдемотиватор")
else:
    message("Также, команда требует агрумента -- верхнего и нижнего текста, разделённого через <<;>>")
