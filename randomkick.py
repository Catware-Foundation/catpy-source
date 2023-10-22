
messagecust(f"ВНИМАНИЕ ВСЕМ ЕПТА!!! {getmention(user_id)} собирается выгнать нахуй случяйново чела по причине руская рулетка!!!", peer_id)
hohlinki = []
for ayeayeayeaye in vk.messages.getConversationMembers(peer_id=peer_id)["items"]:
    if ayeayeayeaye["member_id"] != -176186185:
        hohlinki.append(ayeayeayeaye["member_id"])

hohlinka = randd.choice(hohlinki)
#hohlinka = getid("m00ksim")
messagecust("потенциальный гей для кика обнаружен!!! ", peer_id)

for ayea in range(10):
    messagecust(f"ебучяя русская рулетка произойдет через {10 - ayea}", peer_id)
    time.sleep(1)

vk.messages.removeChatUser(member_id=hohlinka, random_id=rid(), chat_id=event.chat_id)

#message("свое очько кикни блять, а если не хочеш - залезь на ебучий сервер и раскомментируй код)))))))))))")
