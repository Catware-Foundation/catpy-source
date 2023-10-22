Output("Старт обновления...")
procmsg("Подгрузка библиотек...")
import os
from json import dumps
import sys
succ()

for x in os.listdir("commands"):
    if os.path.isfile(f"commands/{x}"):
        InfoMsg(f"Переформатирование команды {x}...")
        procmsg("Чтение...")
        cmd = ReadFF(f"commands/{x}").split("\n")[:7]
        succ()
        procmsg("Выполнение...")
        for a in range(6):
            exec(cmd[a + 1])
        succ()
        procmsg("Сборка...")
        js = dumps({"author": author, "mode": mode, "deps": deps, "identificator": identificator, "command_ru": command_ru, "description": description}, ensure_ascii=False)
        succ()
        procmsg("Создание директории...")
        os.mkdir(f"commands/{identificator}")
        succ()
        procmsg("Перемещение и сохранение файлов...")
        os.rename(f"commands/{x}", f"commands/{identificator}/{x}")
        writeTo(js, f"commands/{identificator}/{identificator}.json")
        succ()
        InfoMsg("Переформатирование завершено!")
        Output("\n\n\n")

Output("Привет, мир!")
