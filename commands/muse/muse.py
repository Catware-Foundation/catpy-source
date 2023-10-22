if str(user_id) in admins:
    setparam(user_id, "appdata/muse-command", parameter)
    setparam(user_id, "stage", "infiniteuse")
    message("Сеанс запущен.")
