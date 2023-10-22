# CatOS-Type Package
author = "aGrIk"
mode = "start"
deps = 'None'
identificator = 'geo'
command_ru = 'гео'
description = 'Команда получения географических координат по точному адресу места. '

try:
    geoinfo = Geocode(parameter)
    vk.messages.send(random_id=rid(),
        peer_id=peer_id,
        message=f"""
По данному запросу найдено: {geoinfo[2]}
Координаты места: {geoinfo[0]}, {geoinfo[1]}

Google Maps: https://maps.google.com/maps?&q={geoinfo[0]},{geoinfo[1]}&spn=0.01,0.01
Яндекс.Карты: https://yandex.ru/maps/?ll={geoinfo[0]},{geoinfo[1]}&pt={geoinfo[0]},{geoinfo[1]}&spn=0.01,0.01&l=sat,skl
OpenStreetMap: https://www.openstreetmap.org/?mlat={geoinfo[0]}&mlon={geoinfo[1]}
Уточните запрос, если место некорректно
""",
        lat=geoinfo[0],
        long=geoinfo[1],
        reply_to=globalid(event.object["conversation_message_id"], peer_id))
except:
    message("Такого места не существует, OpenStreetMap так сказал ☝")
