import os

prm = input("parameter name: ")
vle = input("parameter value: ")

fle = open("catenv.py", "r")
exec(fle.read())
fle.close()

users = os.listdir("users")

for x in users:
    writeTo(vle, "users/" + x + "/" + prm + ".txt")
