covidsitehtml = Get('https://стопкоронавирус.рф/information/').encode('cp1251').decode('cp1251')
# обработка с помощью BeatifulSoup и получение нужной строки
soup = BeautifulSoup(covidsitehtml, 'lxml')
find_ = soup.find('cv-stats-virus')
# надо удалить 1 мб бесполезного мусора
del soup, covidsitehtml
# Обработка полученной строки для дальнейшей работы с данными
statdict = eval(str(find_).replace(r"<cv-stats-virus :charts-data='[",
                           "").replace("'></cv-stats-virus>", '').replace(']', '').replace("' :stats-data='", ","))
# работаем с получившимся словарем
date = statdict[0]['date']
statistic = statdict[-1]
# отправка статистики
message(f'''Статистика коронавируса по России на {date}:
Новых случаев: {statistic['sickChange'].replace("+", "")}
Новых смертей: {statistic['diedChange'].replace("+", "")}
Вылечившихся за день: {statistic['healedChange'].replace("+", "")}
Всего случаев: {statistic['sick']}
Всего смертей: {statistic['died']}
Всего вылечившихся: {statistic['healed']}

Вакцинация в России:
Вакцинированы первым компонентом: {statistic['vaccineFirst']}
Вакцинированы полностью: {statistic['vaccineSecond']}
''', reply=True)