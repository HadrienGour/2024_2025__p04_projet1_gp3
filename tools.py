from data import*

def is_in_selected_base (number, base):
    if base == 2:
        valid_chars = bin_valid_chars
    elif base == 10:
        valid_chars = dec_valid_chars
    elif base == 16:
        valid_chars = hex_valid_chars
    else:
        print ("Cette base n'est pas supportée dans le programme")
        return False
    
    
    for j in number:
        if j.upper() in valid_chars:
            pass
        else:
            print ("Le nombre n'existe pas dans cette base")
            return False
    return True


def dec_to_bin (n):
    n = int(n)
    k=""
    while n != 0:
        k = f"{n % 2}"+ k
        n = n//2
    return k

def bin_to_dec (n):
    j = 0
    k = 0
    for i in n[::-1]:
        i = int(i)
        k += i*(2**j)
        j += 1
    return str(k)

def dec_to_hex (n):
    n = int(n)
    k = ""
    if n == 0:
        return 0
    while n != 0:
        k = f"{hex_valid_chars[n % 16]}" + k
        n = n // 16
    return k



def hex_to_dec(hex_number):
    j = 0
    k = 0
    for i in hex_number[::-1]:
        i = hex_valid_chars.index(i.upper())
        k += i*(16**j)
        j += 1
    return str(k)

def bin_to_hex (n):
    return dec_to_hex(bin_to_dec(n))

def hex_to_bin (n):
    return dec_to_bin(hex_to_dec(n))

print(hex_to_bin("9d"))