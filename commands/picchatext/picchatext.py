#CatOS-Type Package
author = "awoo.sh, catwared, aGrIk"
mode = "="
deps = "None"
identificator = "picchatext"
command_ru = "цитата"
description = "Генерирует цитату из сообщения"

text = parameter
try:
    if event.object["reply_message"] != {} and parameter == replytext:
        if not isgroup(event.object["reply_message"]["from_id"]):
            uid = event.object["reply_message"]["from_id"]
            text = replytext
        else:
            uid = user_id
    elif "fwd_messages" in event.object.keys() and parameter == replytext:
        if not isgroup(event.object["fwd_messages"][0]["from_id"]):
            uid = event.object["fwd_messages"][0]["from_id"]
            text = replytext
        else:
            uid = user_id
    else:
        uid = user_id
except:
    uid = user_id

if text == "":
    text = "..."

if ReadFF("argv_picture.txt") == "none":
    ava = vk.users.get(user_ids=uid, fields="photo_max_orig")[0]["photo_max_orig"]
else:
    ava = ReadFF("argv_picture.txt")
#name = vk.users.get(user_ids=uid)[0]
#name = name["first_name"] + " " + name["last_name"]
name = getname(user_id)
if ava.endswith(".png"):
    covyrat_eto_ebychee_pillow = False
else:
    Download(ava, "usr/download.jpg")
    img = Image.open("usr/download.jpg")
    covyrat_eto_ebychee_pillow = True
    width, height = img.size

if covyrat_eto_ebychee_pillow:
    basewidth = 1000
    ratio = (basewidth / float(img.size[0]))
    height = int((float(img.size[1]) * float(ratio)))
    img = img.resize((basewidth, height), Image.ANTIALIAS)
    img.save("usr/image.png", "PNG")

    img = Image.open("usr/image.png")
    width, height = img.size

    resize_image("usr/mask2.png", "usr/mask3.png", (width, height))
    watermark = Image.open("usr/mask3.png")
    img.paste(watermark, (0,0), watermark)

    coef_pix = int(width + height / 2 - int(width + height / 2 / 1.8))
    coef_pix = coef_pix / 2

    img = img.filter(ImageFilter.GaussianBlur(radius = 10))

    font = ImageFont.truetype(font="usr/inter.ttf", size=int(coef_pix / 2))
    #emojifont = ImageFont.truetype(font="usr/AppleColorEmoji.ttf", size=int(coef_pix / 2))

    #text = "\n".join(textwrap.wrap(text, width=int(width / int(int(coef_pix / 3) / 2)), replace_whitespace=False))
    text = "\n".join(textwrap.wrap(text, width=20))

    Text = ImageDraw.Draw(img)
    w, h = Text.textsize(text, font=font)

    drawText = ImageDraw.Draw(img)
    center1 = int(width / 2 - int(w / 2))
    center2 = int(height / 2 - int(h / 2))

    if h > height:
        message("Текст не помещается в пикчу.", reply=True)
    else:
        drawText.multiline_text((center1,center2), text, fill="white", font=font, align="center")
        #drawText.multiline_text((coef_pix, coef_pix), "Золотые слова!", fill="white", font=font, align="center")
        drawText.multiline_text((coef_pix, height - int(coef_pix - 2)), " - " + name, fill="white", font=font, align="center")
        img.save("usr/picchatext.png")
        picturedata("usr/picchatext.png", "Ваша цитата:")
else: message("Не работает для людей без аватарки (пока)", reply=True)

#
# 2020-2021 (c) BlackCat Software
#
