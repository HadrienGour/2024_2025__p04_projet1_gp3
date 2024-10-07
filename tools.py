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
        if j in valid_chars:
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

print (dec_to_hex ("0"))