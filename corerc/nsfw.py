if peer_id == 2000000299 and event.object["attachments"]:
    #ret = "NSFW Analysis - результаты анализа вложений:\n"
    ph = 0
    for x in event.object["attachments"]:
        if x["type"] == "photo":
            ph += 1
            req = requests.post("https://api.deepai.org/api/nsfw-detector", data={'image': detectfull(x)}, headers={'api-key': 'ключик апи'})
            if req.json()["output"]["nsfw_score"] >= 0.85:
                vk.messages.removeChatUser(member_id=user_id, random_id=rid(), chat_id=299)
                vk.messages.delete(peer_id=peer_id, conversation_message_ids=str(event.object['conversation_message_id']), delete_for_all=1)
                message(f"[nsfw] В сообщении {getmention(user_id, 'gen', False)} обнаружена обнажёнка. Сообщение удалено.\n\nВероятность наличия NSFW - {round(req.json()['output']['nsfw_score'] * 100)}%", reply=False, disable_mentions=0)
            else:
                continue
    #if ph > 0:
    #    message(ret)
