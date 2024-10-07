from tools import *
from data import *

def nbr_base_to_nbr_base (init_number, init_base, target_base):
    if is_in_selected_base(init_number, init_base) == True:
        if target_base == 2:
            if init_base == 10:
                target_number = dec_to_bin (init_number)
            elif init_base == 16:
                target_number = hex_to_bin(init_number)
        if target_base == 10:
            if init_base == 2:
                target_number = bin_to_dec (init_number)
            elif init_base == 16:
                target_number = hex_to_dec(init_number)
        if target_base == 16:
            if init_base == 2:
                target_number = bin_to_hex (init_number)
            elif init_base == 10:
                target_number = dec_to_hex(init_number)
    return target_number

def do_the_job ():
    init_number = ask_for_the_init_number
    init_base = ask_for_the_init_base
    target_base = ask_for_the_target_base
    target_number = \
      nbr_base_to_nbr_base (init_number, \
                            init_base, \
                            target_base)

do_the_job ()