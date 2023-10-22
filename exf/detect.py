important_variables = ["cmd", "parameter", "authors", "commands", "ids", "descs", "modes", "depends", "codes", "restricted"]
check_files = ["catenv.py", "core.py", "faststart.py"]
check_directories = ["commands", "experimental", "lib", "corerc", "services", "exf"]

Output(">>> Ищу упоминания...")
for l in check_files:
    for d in important_variables:
        if d in ReadFF(l):
            Output("Обнаружено упоминание: " + l + ", упоминание: " + d)
for l in check_directories:
    for m in os.listdir(l):
        for d in important_variables:
            if d in ReadFF(f"{l}/{m}"):
                Output("Обнаружено упоминание: " + l + "/" + m + ", упоминание: " + d)
