if peer_id == 2000000476:
    if re.findall(r"\b[дДdD][AАаа]+[^\wБ-Яб-яёЁ]*$\Z", event.object["text"]):
        message("Пизда")