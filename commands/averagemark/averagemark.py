try:
    marks = []
    for mark in parameter.split(" "):
        marks.append(int(mark))
    average = round(sum(marks) / len(marks), 2)
    message(f"Оценки: {parameter} ({len(marks)})\nСредняя оценка: {average} (с учётом округления - {round(average)})")
except:
    message("Неправильно введены оценки. Пример: 5 4 5 4 3 2 5 5 3 4 3")