# CatOS-Type Package
author = "CatWeird"
mode = "pic"
deps = 'None'
identificator = 'koncha'
command_ru = 'кончил'
description = 'Подрочить на фотку'

try:
    try:
        argv1 = event.object['attachments'][0]['photo']['sizes'][len(event.object['attachments'][0]['photo']['sizes'])-1]['url']
    except Exception:
        argv1 = event.object['reply_message']['attachments'][0]['photo']['sizes'][len(event.object['attachments'][0]['photo']['sizes'])-1]['url']
    Download(argv1, 'file1.jpg')
    watermark = Image.open('usr/sperm.png')
    width1, height1 = watermark.size
    resize_image('file1.jpg', 'file1.jpg', (width1, height1))
    img = Image.open('file1.jpg')
    width, height = img.size

    img.paste(watermark, (height1-height, width-width1), watermark)
    img.save("result.png")
    picturedata('result.png', 'Вот твоя картинка:')
    os.remove('file1.jpg')
except Exception as e:
    message('Ошибка: ' + str(e), reply=True)

#restricted
