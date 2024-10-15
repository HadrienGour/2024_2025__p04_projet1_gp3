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


def dec_to_other_base (n, b):
    n = int(n)
    k = ""
    if n == 0:
        return 0
    while n != 0:
        k = f"{hex_valid_chars[n % b]}" + k
        n = n // b
    return k 


def base_to_dec (n, b):
    j = 0
    k = 0
    if n == 0:
        return 0
    for i in n[::-1]:
        i = hex_valid_chars.index (i.upper())
        k += i* (b ** j)
        j += 1
    return str (k)


def bin_to_hex (n):
    return dec_to_other_base (base_to_dec (n, 2), 16)


def hex_to_bin (n):
    return dec_to_other_base (base_to_dec (n, 16), 2)

def beauty_print (init_number, init_base, target_base, target_number):
    return f"Le nombre {init_number} dans la base {init_base} vaut {target_number} dans la base {target_base}"