import os.path

files = []

for xxx in os.listdir("exf"):
    if os.path.isdir("exf/" + xxx):
        pass
    else:
        files.append(xxx[:-3])

Output("\n".join(files))
