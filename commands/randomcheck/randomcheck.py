# CatOS-Type Package
author = "aGrIk"
mode = "start"
deps = 'None'
identificator = 'randomcheck'
command_ru = 'мощности'
description = 'Проверка мощностей бота и справедливости рандомайзера. Синтаксис: мощности [итерации] [погрешность]'

#hide
if str(user_id) in admins:
	message("Замер...")
	startd = time.time()
	par = parameter.split(" ")

	itera = int(par[0])
	quaiter = itera / 4
	greh = quaiter / 100 * int(par[1])
	arr = [0, 0, 0, 0]
	res = [False, False, False, False]

	if str(user_id) in admins:

		for i in range(itera):
			a = randd.randint(1, 100)
			if 1 <= a <= 25: arr[0] += 1
			if 26 <= a <= 50: arr[1] += 1
			if 51 <= a <= 75: arr[2] += 1
			if 76 <= a <= 100: arr[3] += 1


		if quaiter - greh <= arr[0] <= quaiter + greh: res[0] = True
		if quaiter - greh <= arr[1] <= quaiter + greh: res[1] = True
		if quaiter - greh <= arr[2] <= quaiter + greh: res[2] = True
		if quaiter - greh <= arr[3] <= quaiter + greh: res[3] = True

		message("Проверка завершена за " + str(int(time.time() - startd)) + """ секунд
	Параметры: """ + str(parameter) + """
	Результат: """ + str(arr) + """
	""" + str(res), reply=True)

#hide
