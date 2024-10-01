from tools import *
from data import *

def nbr_base_to_nbr_base (init_number, init_base, target_base):
    if is_in_selected_base(init_number, init_base) == True:
        if target_base == 2:
            if init_base == 10:
                target_number = dec_to_bin (init_number, init_base)
    return target_number

assert nbr_base_to_nbr_base ("101", 2, 10) == "5"

def do_the_job ():
    init_number = ask_for_the_init_number
    init_base = ask_for_the_init_base
    target_base = ask_for_the_target_base
    target_number = \
      nbr_base_to_nbr_base (init_number, \
                            init_base, \
                            target_base)

do_the_job ()