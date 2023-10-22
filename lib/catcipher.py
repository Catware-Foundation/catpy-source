
#
# -*- coding: utf-8 -*-
#
# Catware Cipher
#

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except Exception as e:
        return str(e)
def decipher(a):
    a = a.replace("%", "##")
    a = a.replace("@", "#&")
    a = a.replace("$", "#*")
    a = a.replace("§", "#?")
    a = a.replace("£", "&&")
    a = a.replace("¢", "&#")
    a = a.replace("€", "&?")
    a = a.replace("¥", "&*")
    a = a.replace("×", "**")
    a = a.replace("÷", "*#")
    a = a.replace("√", "*?")
    a = a.replace("∆", "*&")
    a = a.replace("μ", "??")
    a = a.replace("~", "?#")
    a = a.replace("<", "?&")
    a = a.replace(">", "?*")
    a = a.replace("#", "00")
    a = a.replace("&", "01")
    a = a.replace("*", "10")
    a = a.replace("?", "11")
    a = a.replace("1", 'a')
    a = a.replace('0', 'b')
    a = a.replace('b', '1')
    a = a.replace('a', '0')
    a = text_from_bits(a)
    return a
def cipher(a):
    a = text_to_bits(a)
    a = a.replace("1", 'a')
    a = a.replace('0', 'b')
    a = a.replace('b', '1')
    a = a.replace('a', '0')
    a = a.replace("00", "#")
    a = a.replace("01", "&")
    a = a.replace("10", "*")
    a = a.replace("11", "?")
    a = a.replace("##", "%")
    a = a.replace("#&", "@")
    a = a.replace("#*", "$")
    a = a.replace("#?", "§")
    a = a.replace("&&", "£")
    a = a.replace("&#", "¢")
    a = a.replace("&?", "€")
    a = a.replace("&*", "¥")
    a = a.replace("**", "×")
    a = a.replace("*#", "÷")
    a = a.replace("*?", "√")
    a = a.replace("*&", "∆")
    a = a.replace("??", "μ")
    a = a.replace("?#", "~")
    a = a.replace("?&", "<")
    a = a.replace("?*", ">")
    return a
