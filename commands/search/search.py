req = requests.get(f"https://searx.roughs.ru/search?q={parameter}&format=json&source_from=ctwre.ru&categories=general&safesearch=1").json()

ret = "Первые результаты поиска:"

if req["results"]:
    for ayeaye in req["results"][:4]:
        ret += f"""
{ayeaye['title']}
"""
        if "content" in ayeaye.keys():
            ret += f"{ayeaye['content']}"
        ret += f"""
Ссылка:
{ayeaye["url"]}


"""
else:
    ret = "Ничего не найдено."

message(ret)
