# CatOS-Type Package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'console'
command_ru = 'exec'
description = 'Консоль [только для администраторов]'
#hide

if str(user_id) in admins:
    try:
        exec(parameter)
        if not "-no_ok" in flags: message('ok')
    except Exception as err:
        exc_type, exc_value, exc_tb = sys.exc_info()
        message('Error: \n' + "\n".join(traceback.format_exception(exc_type, exc_value, exc_tb)))
else:
    message("Вы не были обнаружены в списке администраторов.")