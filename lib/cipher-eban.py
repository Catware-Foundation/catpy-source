
#
# Catware Eban Cipher Library
#
#
#def TextToBits(text, encoding='utf-8', errors='surrogatepass'): # Text to 101010010100101
#    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
#    return bits.zfill(8 * ((len(bits) + 7) // 8))
#
#def TextFromBits(bits, encoding='utf-8', errors='surrogatepass'): # Text from 10101001010101
#    try:
#        n = int(bits, 2)
#        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
#    except Exception:
#        return 'error'
#
#def encode(text):
#    pattern = str(TextToBits(text))
#    pattern = pattern.replace("00", "ауе")
#    pattern = pattern.replace("11", "semen")
#    pattern = pattern.replace("01", "хуй")
#    pattern = pattern.replace("10", "gay")
#    return pattern
#
#def decode(text):
#    pattern = pattern.replace("ауе", "00")
#    pattern = pattern.replace("semen", "11")
#    pattern = pattern.replace("хуй", "01")
#    pattern = pattern.replace("gay", "10")
#    pattern = str(TextFromBits(pattern))
#    return pattern
