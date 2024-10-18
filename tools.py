from data import*

def is_in_selected_base (number, base):
    if base == 2:
        valid_chars = bin_valid_chars
    elif base == 10:
        valid_chars = dec_valid_chars
    elif base == 16:
        valid_chars = hex_valid_chars
    else:
        return "not a base"
    
    
    for j in number:
        if j.upper() in valid_chars:
            pass
        else:
            return "not in selected base"
    return True


def dec_to_other_base (number, target_base):
    number = int(number)
    target_number = ""
    if number == 0:
        return 0
    while number != 0:
        target_number = f"{hex_valid_chars [number % target_base]}" + target_number
        number = number // target_base
    return target_number


def base_to_dec (number, target_base):
    exponent = 0
    target_number = 0
    if number == 0:
        return 0
    for digit in number[::-1]:
        digit = hex_valid_chars.index (digit.upper())
        target_number += digit * (target_base ** exponent)
        exponent += 1
    return str (target_number)


def bin_to_hex (number):
    return dec_to_other_base (base_to_dec (number, 2), 16)


def hex_to_bin (number):
    return dec_to_other_base (base_to_dec (number, 16), 2)

def beauty_print (init_number, init_base, target_base, target_number):
    return f"Le nombre {init_number} dans la base {init_base} vaut {target_number} dans la base {target_base}"