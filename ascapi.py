
#
# ASCAPI (Advanced Software Select Application Programming Interface)
#
# Defintion kit that gives you an easy way to interact with the SS system
#

try:
    al = current_application
    del al
except:
    current_application = "lost"
    try:
        os.mkdir(f"users/{str(user_id)}/appdata/lost")
    except:
        pass

def ss_write(data, filename, current_application=current_application):
    if "/" in filename:
        return "ASCAPI Error: иди нахуй, у нас пути запрещены блядь"
    else:
        writeTo(data, f"users/{str(user_id)}/appdata/{current_application}/{filename}")

def ss_read(filename):
    if "/" in filename:
        return "ASCAPI Error: иди нахуй, у нас пути запрещены блядь"
    else:
        return ReadFF(f"users/{str(user_id)}/appdata/{current_application}/{filename}")

def ss_regapp(appid, pers="empty"):
    os.mkdir("users/{str(user_id)/appdata/{appid}")
    ss_write(pers, "persmissions.txt", current_application=appid)

#def ss_registerpersmission(appid, name):
#    #
#    # Persmissions: write, read, install, delete
#    # Format: persmission,persmission,persmission
#    #
#    if ss_read("
