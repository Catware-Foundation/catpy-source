vk2 = VkApi(token="77235ec95e745b9fdeeb1664a07805ecbc224a612b29ccacc32d8cd31220631012cedbfe78cdd92e8d3fe", api_version="5.131").get_api()

message("чё надо дай поспать", reply=False)
message("лан ща", reply=False)

liks = vk2.likes.getList(type="post", owner_id=-176186185, item_id=3479, filter="likes")["items"]
ret = ""
"""
for aye in liks:
    ret += f'{getmention(aye)}\n'

message(f"Лайки поставили:\n{ret}", reply=False)
"""
comments = vk2.wall.getComments(owner_id=-176186185, post_id=3479, count=100)["items"]
coms = []
ret = ""
for aye in comments:
    if aye["from_id"] > 0 and aye["from_id"] not in coms:
        #ret += f'{getmention(aye["from_id"])}\n'
        coms.append(aye["from_id"])

#message(f"Прокомментировали:\n{ret}", reply=False)

subs = []
ret = ""
for aye in liks:
    if vk.groups.isMember(user_id=aye, group_id="catpy") == 1:
        #ret += f'{getmention(aye)}\n'
        subs.append(aye)

#message(f"Подписаны:\n{ret}", reply=False)

active = []
ret = ""
for aye in liks:
    if getparam(aye, "score") != None and int(getparam(aye, "score")) >= 50:
        #ret += f'{getmention(aye)}\n'
        active.append(aye)

#message(f"Больше 50 команд использовали:\n{ret}", reply=False)


sort = []
ret = ""
for aye in liks:
    if aye in coms and aye in subs and aye in active:
        sort.append(aye)
        ret += f'{getmention(aye)}\n'

message(f"Все условия выполнили:\n{ret}", reply=False)

winner = randd.choice(sort)
message(f"Стикеры получает {getmention(winner)}", reply=False)