if str(user_id) in admins:
    endl = "\n"
    setparam(user_id, "appdata/explorer-directory", f"users/{str(user_id)}")
    message(f"""Добро пожаловать в Catpy Explorer, господин {getname(user_id)}.
Директория: {getparam(user_id, 'appdata/explorer-directory')}
Список файлов - - - - - - - - - - - -
{endl.join(os.listdir(getparam(user_id, 'appdata/explorer-directory')))}
- - - - - - - - - - - - - - - - - - -
cd <директория> - сменить директорию.
nv <файл> - установить содержимое файла.
py <команда> - выполнить строчку на питоне.
show <файл> - показать содержимое файла.
exit - выйти из Catpy Explorer.""")
setparam(user_id, "stage", "exp")
