# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'ip'
command_ru = 'вычислить1'
description = 'Вычислить человека по IP'

#hide
#disable

try:
    inform = Get("http://api.db-ip.com/v2/free/" + parameter)
    inform = str(inform)
    message("IP: " + inform['ipAddress'] + '\nСтрана: ' + inform['countryName'] + '\nГород: ' + inform['city'], reply=True)
except:
    message('Не удалось вычислить человека.\n' + str(e), reply=True)