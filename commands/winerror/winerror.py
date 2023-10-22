parameter = parameter.split(";")
try:
    picture(f"http://atom.smasher.org/error/xp.png.php?style=xp&title={parameter[0]}&url=&text={parameter[1]}&b1={parameter[2]}&b2={parameter[3]}&b3={parameter[4]}", "Ошибка готова:")
except:
    message("Вероятно, вы неправильно используете команду. Правильное использование: заглавие;текст;кнопка1;кнопка2;кнопка3. Некоторые значения можно оставлять пустыми. Пример использования: \n\nошибка catpy;Some error was happened;OK;No;;\n\nТакже нужно учесть, что все параметры должны быть на английском языке.")
