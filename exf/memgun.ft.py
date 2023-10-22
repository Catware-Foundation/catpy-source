vars = dir()
yyy = []
for xx in vars:
    try:
        exec(f"if parameters_ in {str(xx)}: yyy.append('{str(xx)}')")
    except:
        pass
Output("Найдены переменные с упоминанием: " + "\n".join(yyy))
