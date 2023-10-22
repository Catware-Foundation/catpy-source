
#
# Catware REport MTA
#
# Written Specially for report command.
#

def mtapicture(URL, text):
    random_id = randd.randint(-2147483647, 2147483647)
    pic = str(URL)
    #message("Loading...") <- Как же за##ало это сообщение...
    try:
        try:
            attachments = []
            upload = VkUpload(vk_session)
            image_url = pic
            image = session.get(image_url, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachments.append(
                'photo{}_{}'.format(photo['owner_id'], photo['id'])
            )
            vk.messages.send(
            random_id=random_id,
            user_ids=ReadFF('admins.txt'),
            message=str(text).replace("vto.pe", '').replace("vkbot.ru", '')[:4000],
            attachment=','.join(attachments),
			dont_parse_links=1
            )
        except Exception:
            message(str(text))
    except Exception as e:
        #mta(e)
        pass