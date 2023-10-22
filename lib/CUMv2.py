
#
# Catware User Manager v2 (CUMv2)
#
# Library for accessing user's accounts parameters: get, change.
#

def getparam(user, param):
    try:
        return ReadFF(f"users/{str(user)}/{str(param)}.txt")
    except:
        return "CUMv2 Error: User or parameter not found."

def setparam(user, param, value):
    try:
        writeTo(value, f"users/{str(user)}/{str(param)}.txt")
        return "Success"
    except:
        return "CUMv2 Error: Unable to write (user not found)."
