if str(user_id) in admins:
    output_to_message = True
    wrds = parameter.split(" ")
    command = wrds[0]
    parameters_ = " ".join(wrds[1:])
    writeTo(parameters_, 'exf/parameters.txt')
    try:
        if command == "exit":
            session_console = False
        else:
            exec(ReadFF('exf/' + command + '.py'))
    except Exception as e:
        if command + '.py' not in os.listdir('exf'):
            message('/' + 'exf/' + command + '.py: command not found')
        else:
            message('/' + 'exf/' + command + '.py crushed with error: ' + str(e))
    output_to_message = False
else:
    message("Вы не обнаружены в списке администраторов")
