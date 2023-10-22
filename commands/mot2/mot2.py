# CatOS-type package
author = "Anton2319"
command_ru = "мотиватор"
deps = "None"
identificator = "mot2"
description = "Как демотиватор, только мотиватор"
mode = "pic"
#disable
try:
    try:
        text1, text2 = parameter.split(";")[0], parameter.split(";")[1]
    except:
        text1, text2 = parameter, ""
except:
    text1, text2 = "блять текст забыл.", "ладно."

if text2 == "":
    text2 = "  "

Download(ReadFF("argv_picture.txt"), "usr/download.jpg")

img = Image.open("usr/download.jpg")
width, height = img.size

coef_pix = int(width + height / 2 - int(width + height / 2 / 1.7))

if width * height < 350 or width * height < 60000:
    img.save("usr/download.jpg")
    resize_image("usr/download.jpg", "usr/download.jpg", (width * coef_pix, height * coef_pix))
    img = Image.open("usr/download.jpg")
    width, height = img.size

font1 = ImageFont.truetype(font="usr/demfont.ttf", size=int(coef_pix / 2), encoding="unic")
font2 = ImageFont.truetype(font="usr/demfont2.ttf", size=int(coef_pix / 3), encoding="unic")

#if imagetext.size[1] > height+coef_pix:
#    wid = imagetext.size[0]
#else:
wid = width+coef_pix#+imagetext.size[0]

text1 = "\n".join(textwrap.wrap(text1, width=18))
text2 = "\n".join(textwrap.wrap(text2, width=20))

notformatted = True
drawtext = ImageDraw.Draw(img)
w1, h1 = drawtext.textsize(text1, font=font1)
w2, h2 = drawtext.textsize(text2, font=font2)
del drawtext

#if imagetext.size[1] > height+coef_pix:
#    heighd = imagetext.size[1]
#else:
heighd = height+coef_pix+h1+h2+int(int(coef_pix / 3) * 1.1)

imagetext = Image.new("RGB", (int(width+int(coef_pix*2)), h1+h2+90+int(coef_pix*2)), (0,0,255,0))
imagetextd = ImageDraw.Draw(imagetext)
need = int(imagetext.size[0] / 3.7 - int(w2 / 2))
# готово нахуй, суём это
center1 = int(wid / 2 - int(w1 / 2))
center2 = int(wid / 2 - int(w2 / 2))
imagetextd.multiline_text((center1,5), text1, fill="white", font=font1, align="center")
imagetextd.multiline_text((center2,5+h1+10), text2, fill="white", font=font2, align="center")
#module_center = int(imagetext.size[0] / 2)

image = Image.new("RGB", (wid,heighd), (0,0,255,0))
shape = [(width+int(coef_pix / 2) + 3,height+int(coef_pix / 2) + 3),(int(coef_pix / 2) - 2,int(coef_pix / 2) - 2)]
draw = ImageDraw.Draw(image)
draw.rectangle(shape, outline="white")
image.paste(img, (int(coef_pix / 2) + 1, int(coef_pix / 2) + 1))
#image.paste(imagetext, (int(image.size[0] / 1.8) - int(imagetext.size[0] / 3), height + int(coef_pix / 2 + int(coef_pix / 2) - int(coef_pix / 4))))
image.paste(imagetext, (0, height + int(coef_pix / 2 + int(coef_pix / 2) - int(coef_pix / 4))))
image.save("usr/mot.jpg")
picturedata("usr/mot.jpg", "Ваш мотиватор готов:")
