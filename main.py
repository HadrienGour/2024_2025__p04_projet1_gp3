from tools import *
from data import *

def nbr_base_to_nbr_base (init_number, init_base, target_base):
    if target_base == 2:
        if init_base == 10:
            target_number = dec_to_other_base (init_number, target_base)
        elif init_base == 16:
            target_number = hex_to_bin (init_number)
        else:
            target_number = init_number
    elif target_base == 10:
        target_number = base_to_dec (init_number, init_base)
    elif target_base == 16:
        if init_base == 2:
            target_number = bin_to_hex (init_number)
        elif init_base == 10:
            target_number = dec_to_other_base (init_number, target_base)
        else:
            target_number = init_number
    else:
        return False
    return target_number

def do_the_job (init_number, init_base, target_base):
    quit_or_continue = "continue"
    while quit_or_continue not in quit_responses:
        if is_in_selected_base (init_number, init_base) == True:
            target_number = nbr_base_to_nbr_base (init_number, init_base, target_base)
            if target_number != False:
                target_number = beauty_print (init_number, init_base, target_base, target_number)
                print( target_number ) 
            else:
                print ( base_error)
        elif is_in_selected_base (init_number, init_base) == "not a base":
           print ( base_error )
        elif is_in_selected_base (init_number, init_base) == "not in selected base":
           print ( number_error )
        quit_or_continue = str(input("souhaitez vous continuer ? : "))
        if quit_or_continue not in quit_responses:
            init_number = str(input("entrez le nombre initial :"))
            init_base = int(input("entrez la base de ce nombre (2, 10, 16) :"))
            target_base = int(input("entrez la base dans laquelle vous souhaitez passer ce nombre (2, 10, 16) :"))
    return "end of program"

do_the_job (ask_for_the_init_number, ask_for_the_init_base, ask_for_the_target_base)