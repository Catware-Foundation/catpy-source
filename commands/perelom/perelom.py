# CatOS-Type Package
author = "catwared"
mode = "pic"
deps = 'None'
identificator = 'perelom'
command_ru = 'перелом'
description = 'Сломать фотографию'

try:
    try:
        argv2 = event.object['attachments'][0]['photo']['sizes'][len(event.object['attachments'][0]['photo']['sizes'])-1]['height']
    except Exception:
        argv2 = event.object['reply_message']['attachments'][0]['photo']['sizes'][len(event.object['attachments'][0]['photo']['sizes'])-1]['height']
    try:
        argv1 = event.object['attachments'][0]['photo']['sizes'][len(event.object['attachments'][0]['photo']['sizes'])-1]['url']
    except Exception:
        argv1 = event.object['reply_message']['attachments'][0]['photo']['sizes'][len(event.object['attachments'][0]['photo']['sizes'])-1]['url']
    try:
        os.remove('file1.jpg')
    except Exception:
        pass
    Download(argv1, 'file1.jpg')
    im = Image.open('file1.jpg')
    dst_grid = griddify(shape_to_rect(im.size), 4, 4)
    src_grid = distort_grid(dst_grid, int(argv2 / 9.2))
    mesh = grid_to_mesh(src_grid, dst_grid)
    im = im.transform(im.size, Image.MESH, mesh)
    im.save("result.png")
    picturedata('result.png', 'картинка готова. Сила переламывания = ' + str(int(argv2 / 9.2)))
    os.remove('file1.jpg')
except Exception as e:
    message('Ошибка: ' + str(e), reply=True)
