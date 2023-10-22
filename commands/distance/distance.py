if not parameter:
    message("""Команда "расстояние" измеряет расстояние между двумя объектами, разделёнными через точку с запятой.
Пример:
/расстояние Москва;Киров
/расстояние 55.7504461, 37.6174943;58.6035257, 49.6639029
    """)
else:
    objcts = parameter.split(";")
    if len(objcts) == 2:
        try:
            geo = []
            geo.append(tuple(Geocode(objcts[0])))
            geo.append(tuple(Geocode(objcts[1])))
            message(f"Расстояние между {geo[0][2]} ({geo[0][0]}, {geo[0][1]}) и {geo[1][2]} ({geo[1][0]}, {geo[1][1]}) составляет {round(distance.distance(geo[0][:2], geo[1][:2]).km, 2)} км")
        except:
            message("Ошибка: объекты не найдены.")

    else:
        message("Должно быть два объекта.")
