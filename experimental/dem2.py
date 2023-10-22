# CatOS-type package
author = "catweird"
command_ru = "демотиватор"
deps = "None"
identificator = "dem2"
description = "Создание демотиваторов. Используйте ; для разделения текста"
mode = "pic"

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

pattern = Image.open('usr/demotivator.jpg')
font1 = ImageFont.truetype(font="usr/demfont.ttf", size=int(coef_pix / 2), encoding="unic")
font2 = ImageFont.truetype(font="usr/demfont.ttf", size=int(coef_pix / 3), encoding="unic")

notformatted = True
back1, back2 = text1, text2
drawtext = ImageDraw.Draw(img)
cl1 = 0
cl2 = 0

#while notformatted:
w1, h1 = drawtext.textsize(text1, font=font1)
w2, h2 = drawtext.textsize(text2, font=font2)
#    if w1 > width + coef_pix * 2 and h1 > height + coef_pix * 2:
#        cl1 += 1
#        cl2 += 1
#        text1 = back1[len(back1) - 1 + cl1] + back1[len(back1)-1-len(text1)-1]
#        text2 = back2[len(back2) - 1 + cl2] + back2[len(back2)-1-len(text2)-1]
#    else:
#        notformatted = False

#del drawtext

#if imagetext.size[1] > height+coef_pix:
#    heighd = imagetext.size[1]
#else:
heighd = height+coef_pix+imagetext.size[1]

#if imagetext.size[1] > height+coef_pix:
#    wid = imagetext.size[0]
#else:
wid = width+coef_pix#+imagetext.size[0]

imagetext = Image.new("RGB", (int(width+coef_pix), h1+h2*2), (0,0,0,0))
imagetextd = ImageDraw.Draw(imagetext)
need = int(imagetext.size[0] / 3.7 - int(w2 / 2))
# готово нахуй, суём это
center1 = int(wid / 2 - int(w1 / 2))
center2 = int(wid / 2 - int(w2 / 2))
imagetextd.multiline_text((center1,5), text1, fill="white", font=font1, align="center")
imagetextd.multiline_text((center2,5+h1+10), text2, fill="white", font=font2, align="center")
#module_center = int(imagetext.size[0] / 2)

image = Image.new("RGB", (wid,heighd), (0,0,0,0))
shape = [(width+int(coef_pix / 2) + 3,height+int(coef_pix / 2) + 3),(int(coef_pix / 2) - 2,int(coef_pix / 2) - 2)]
draw = ImageDraw.Draw(image)
draw.rectangle(shape, outline="white")
image.paste(img, (int(coef_pix / 2) + 1, int(coef_pix / 2) + 1))
#image.paste(imagetext, (int(image.size[0] / 1.8) - int(imagetext.size[0] / 3), height + int(coef_pix / 2 + int(coef_pix / 2) - int(coef_pix / 4))))
image.paste(imagetext, (0, height + int(coef_pix / 2 + int(coef_pix / 2) - int(coef_pix / 4))))
image.save("usr/dem.jpg")
picturedata("usr/dem.jpg", "Ваш демотиватор готов:")