if parameter:
    if len(parameter) <= 25 and parameter.lower() != "хуев":
        writeTo(parameter, f'users/{user_id}/nick.txt')
        message(f"Теперь вам присвоен никнейм {parameter}")
    elif parameter.lower() == "хуев":
        message("окококок умничка!!!!!!!!!")
    else:
        message("Вы превысили ограничение длины никнейма в 25 символов. Придумайте что-нибудь покороче.")
else:
    if os.path.exists(f"users/{user_id}/nick.txt"):
        message(f"Ваш никнейм: {ReadFF(f'users/{user_id}/nick.txt')}")
    else:
        message("У вас пока нет никнейма. Исправить это недоразумение можно при помощи /ник [никнейм]")
