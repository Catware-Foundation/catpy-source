params = parameter.split(";;;")
try:
    if generrorcode(params[0], "a") == generrorcode(params[1], "a"):
        message("Текста схожи между собой")
    else:
        message("Текста не очень похожи друг на друга")
except:
    message("Неправильные параметры. Разделите на ;;;.")
