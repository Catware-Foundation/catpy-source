TABLESTART = """<table border="1">
   <caption>Catware Memory Gun - Gentable at $TIME</caption>
   <tr>
    <th>Название переменной</th>
    <th>Содержимое</th>
    <th>Размер</th>
    <th>Тип</th>
   </tr>"""
TE = "<tr><td>$NAME</td><td>$CONTENT</td><td>$SIZE</td><td>$TYPE</td></tr>"
shot = dir()
tables = []
for g in shot:
    try:
        exec(f"""
if '{g}' != 'tables':
    tables.append(TE.replace('$NAME', '{g}').replace('$CONTENT', str({g}).replace('<', '&lt;').replace('>', '&gt;')).replace('$SIZE', str(sys.getsizeof({g}))).replace('$TYPE', str(type({g})).replace('<', '&lt;').replace('>', '&gt;')))
""")
    except Exception as e:
        tables.append('<h4>Error: ' + str(e) + '</h4>')
htmlcode_ = "<html><head><meta charset='UTF-8'><title>Memgun - Gentable</title></head><body>" + TABLESTART + "\n".join(tables) + "</table></body></html>"
writeTo(htmlcode_, '/home/catpy/server/memgun.html')
Output("Готово")
