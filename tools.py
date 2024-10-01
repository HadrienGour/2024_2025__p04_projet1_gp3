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

if is_in_selected_base(ask_for_the_init_number, ask_for_the_init_base) == True:
    if ask_for_the_target_base == 2:
        if ask_for_the_init_base == 10:
            print(dec_to_bin(ask_for_the_init_number))