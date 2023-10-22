
#
# Catware User Manager v2 (CUMv2)
#
# This is a coz catAPI (a.k.a catnetwork) sucks
#

params = {"score": "0",
 "chats_seen": "", # chat;chat;chat
 "stage": "default",
 "indexfile": "empty"
}

if str(user_id) not in os.listdir('users'):
    try:
        os.mkdir("users/" + str(user_id))
        for lg in params.keys():
            writeTo(params[lg], "users/" + str(user_id) + f"/{lg}.txt")
        os.mkdir(f"users/{str(user_id)}/appdata")
    except Exception as e:
        Output("Ошибка при регистрации пользователя " + str(user_id) + ": " + str(e))
    #mta("[ + ] Новый пользователь: " + getmention(user_id))

# Отключено по причине ауе спам!!! пофиксиш)
