# CatOS-type package
author = "catwared"
mode = "start"
deps = 'None'
identificator = 'knopki'
command_ru = 'кнопки'
description = 'Добавить кнопку в диалог (Используйте флаг -delete для удаления кнопок.)'

#disable

if not event.from_chat:
    if "-delete" not in parameter:
        try:
            keyboard.add_button(parameter, color=VkKeyboardColor.DEFAULT)
        except:
            keyboard.add_line()
            keyboard.add_button(parameter, color=VkKeyboardColor.DEFAULT)
        messagecust(
        keyboard=keyboard.get_keyboard(),
        message='🖲Кнопка добавлена'
        )
    else:
        keyboard = VkKeyboard(one_time=False)
        try:
            keyboard.add_button(parameter.replace("-delete", ""), color=VkKeyboardColor.DEFAULT)
        except:
            keyboard.add_line()
            keyboard.add_button(parameter.replace("-delete", ""), color=VkKeyboardColor.DEFAULT)
        messagecust(
        keyboard=keyboard.get_keyboard(),
        message='Кнопки очищены.'
        )
else:
    message("Данная команда предназначена для лс.", reply=True)
