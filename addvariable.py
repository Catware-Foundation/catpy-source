
#
# CUMv2 Add Variable 
#

import os

file = open("/home/catpy/catabms_52/catenv.py", "r")
exec(file.read())
file.close()

varname = input(" >>> Введите название параметра: ")
defvalue = input(" >>> Введите значение по-умолчанию: ")
directory = input(" >>> Введите название папки: ")

try:
    for k in os.listdir(directory):
        try:
            writeTo(defvalue, f"{directory}/{k}/{varname}.txt")
            #os.mkdir(f"{directory}/{k}/{varname}")
            print(f" >>> Успешно записан: {directory}/{k}/{varname}.txt ")
        except:
            print("Ошибка бледть")
except Exception as e:
    print(f"AV крашнулся, пошёл нахуй рукожоп блять: {str(e)}")
