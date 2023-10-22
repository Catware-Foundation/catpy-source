try:
    devices = []
    handle = False
    for proc in gb_obj["devices"]:
        if parameter.lower() in proc["name"].lower():
            devices.append(f"""Информация о процессоре {proc['name']}

Технические характеристики: {proc['description'].replace('cores', 'ядер')}
Баллы производительности в одноядерном режиме: {proc['score']}
Баллы производительности в многоядерном режиме: {proc['multicore_score']}
Семейство процессоров: {proc['family']}""")
    if len(devices) == 0:
        message("Процессор(ы) не найден(ы).")
    elif len(devices) > 1 and len("Найдены следующие процессоры:\n\n" + "\n- - - - - - - - - - - - - - - - - - - -\n".join(devices)) < 4000:
        message("Найдены следующие процессоры:\n\n" + "\n- - - - - - - - - - - - - - - - - - - -\n".join(devices))
    elif len("Найдены следующие процессоры:\n\n" + "\n- - - - - - - - - - - - - - - - - - - -\n".join(devices)) > 4000:
        URL = requests.post("https://dpaste.com/api/v2/", data={"content": "Найдены следующие процессоры:\n\n" + "\n- - - - - - - - - - - - - - - - - - - -\n".join(devices), "title": "Результат работы /цп"})
        message("Процессоров слишком много, и обычным сообщением ВКонтакте их не отправить: уточните запрос. Но Я всё равно покажу Вам, что я нарыл: " + URL.text)
    else:
        message(devices[0])
except:
    pass
