# requests.post('https://q.ctw.re/api.php', json={"token": "mbf979wt2nfbsp3v", "action": "add", "message": event.object["fwd_messages"]}).text
#message(event.object)
#list(dict.fromkeys(new_menu))
#users:
#[
#{"user_id":1231298,"first_name":"sex","last_name":"spermogrob","ava_url":"https://pornozal.offline"}
#{"user_id":1232423,"first_name":"sesd","last_name":"spermdfsdfgrob","ava_url":"https://pwef.offline"}
#]
from __future__ import print_function
sent = None
def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results
if event.object["fwd_messages"] != []:
    #message(requests.post('https://q.ctw.re/api.php', json={"token": "mbf979wt2nfbsp3v", "action": "add", "message": event.object["fwd_messages"]}).text)
    sent = "fwd_messages"
elif "reply_message" in [*event.object]:
    #message(requests.post('https://q.ctw.re/api.php', json={"token": "mbf979wt2nfbsp3v", "action": "add", "message": event.object["reply_message"]}).text)
    sent = "reply_message"
userdata = []
userslist = list(dict.fromkeys(find_values('from_id', json.dumps(event.object))))
for x in userslist:
    if x > 0:
        inf = vk.users.get(user_ids=id, fields="photo_400_orig")[0]
        avatar = inf["photo_400_orig"]
        fname = inf["first_name"]
        lname = inf["last_name"]
    else:
        
if sent != None:
    requests.post('https://q.ctw.re/api.php', json={"token": "mbf979wt2nfbsp3v", "action": "add", "message": event.object[sent]}).text
#message("так ьля это ещё не всё")
#message(list(dict.fromkeys(find_values('from_id', json.dumps(event.object)))))
