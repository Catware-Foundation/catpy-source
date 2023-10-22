if event.from_chat:
    if str(event.chat_id) not in os.listdir("chats"):
        os.mkdir("chats/" + str(event.chat_id))
        writeTo("Правила не установлены.", "chats/" + str(event.chat_id) + "/rules.txt")
        writeTo("", "chats/" + str(event.chat_id) + "/muted.txt")
