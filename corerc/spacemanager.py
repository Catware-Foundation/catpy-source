
#
# Catware Space Manager
#

succ()
print("CSM (Catware Space Manager) is working...")
ends = [".save", ".save.1", ".save.2", ".save.3", ".save.4", ".save.5"]
ends_delete = [".mp3", ".wav", ".png", ".jpg", ".json"]

try:
    os.mkdir("savedfiles")
except:
    pass

files = os.listdir("tmp")
for k in files:
    os.remove("tmp/" + k)

files = os.listdir(".")
for k in files:
    for j in ends:
        if k.endswith(j):
            try:
                os.rename(k, "savedfiles/" + k + "-catABMS.save")
                print(f"CSM: Moved file {k} to savedfiles/ directory")
            except:
                print("Failed to move.")
for k in files:
    for j in ends_delete:
        if k.endswith(j):
            try:
                os.remove(k)
                print(f"CSM: Deleted file '{k}', because it's has handled as useless/no longer needed file.")
            except:
                print(f"CSM: Failed to delete '{k}'")
