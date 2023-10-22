
#
# Catware String Chunks Library (CSCL)
#
# Splits a string into a list of N characters
#

def chunk(string_, integer_):
    updatable_list = ""
    rs = []
    for j in string_:
        if len(updatable_list) < int(integer_):
            updatable_list += j
        if len(updatable_list) = int(integer_):
            rs.append(updatable_list)
    return rs
