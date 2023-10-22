
#
# историческая хуйня связанная с развалом ФРПИКК в 2021 году
#

for mem in mems:
    if mem > 0 and str(mem) not in admins: 
        try: vk.messages.removeChatUser(chat_id=72, member_id=mem)
        except: pass
