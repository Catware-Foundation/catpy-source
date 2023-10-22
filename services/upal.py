
#
# -*- coding: utf-8 -*-
#
# "I'm fallen" easter egg
#

upload = VkUpload(vk_session)
photo = upload.photo_messages(photos="usr/upal.png")[0]
writeTo('photo{}_{}'.format(photo['owner_id'], photo['id']), "usr/easter-egg.txt")