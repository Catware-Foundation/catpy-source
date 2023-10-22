# CatOS-type package
author = "catweird"
command_ru = "лобстер"
deps = "None"
identificator = "lobster"
description = "Наложение шрифта Lobster на изображение."
mode = "pic"

Download(ReadFF("argv_picture.txt"), "usr/download.jpg")

img = Image.open("usr/download.jpg")
img.save("usr/download.png", "PNG")
img = Image.open("usr/download.png")
width, height = img.size
coef_pix = int(width + height / 2 - int(width + height / 1.9 / 1.7))

font1 = ImageFont.truetype(font="usr/lobster.ttf", size=int(coef_pix / 2.5), encoding="unic")

imagetextd = ImageDraw.Draw(img)
w1, h1 = imagetextd.textsize(parameter, font=font1)
need = height - h1
ncenter = int(width / 2) - int(w1 / 2)

#image = Image.new("RGBA", (w1, h1), (0, 0, 0, 0))
#imagetextd2 = ImageDraw.Draw(image)
#imagetextd2.multiline_text((ncenter,need), parameter, fill="white", font=font1, align="center")
#image.save("tmp/text.png", "PNG")
#newsizewp = w1 / 100
#newsizehp = h1 / 100
#needw = width / newsizewp
#needh = height / newsizehp
#image = image.resize((int(needw), int(needh)))
#os.system("convert black_circle.png  -channel RGBA  -blur 0x8 usr/blur.png")
#blurred_image = Image.open("usr/blur.png")

#img.paste(image, (ncenter, need))
imagetextd.multiline_text((ncenter+1,need), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter,need+1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter+3,need+1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter+2,need+1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter+1,need+1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter-1,need), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter,need-1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter-1,need-1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter-2,need-1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter-3,need-1), parameter, fill="black", font=font1, align="center")
imagetextd.multiline_text((ncenter,need), parameter, fill="white", font=font1, align="center")
img.save("usr/lobster.png")
#image.close()
if str(ncenter).startswith("-"):
    picturedata("usr/lobster.png", "Я заметил, что текст не влазит и ушёл за грань, поэтому попробуйте перенести строку. Ваше изображение, кстати:")
else:
    picturedata("usr/lobster.png", "Ваше изображение:")
