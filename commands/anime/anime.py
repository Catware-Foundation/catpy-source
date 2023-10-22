req = requests.post("https://api.deepai.org/api/toonify", data={"image": ReadFF("argv_picture.txt")}, headers={'api-key': 'какой то токен'})
message(req.json())
