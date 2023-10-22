if event.from_user:
    endl = "\n"
    greet = f"""Добро пожаловать в Catpy FOD - Поле Чудес в Catpy.

Список категорий:
{endl.join(categories)}

Напишите полное название категории, на которую вы хотите выбрать слово (чувствительно к регистру)
"""
    message(greet)
    setparam(user_id, "stage", "fod1")
else:
    message("Я вам запрещаю играть в Поле Чудес в беседах.")
