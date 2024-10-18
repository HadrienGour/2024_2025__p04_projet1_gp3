from tools import *
from data import *

def nbr_base_to_nbr_base (init_number, init_base, target_base):
    if target_base == 2:
        if init_base == 10:
            target_number = dec_to_other_base (init_number, target_base)
        elif init_base == 16:
            target_number = hex_to_bin (init_number)
    if target_base == 10:
        target_number = base_to_dec (init_number, init_base)
    if target_base == 16:
        if init_base == 2:
            target_number = bin_to_hex (init_number)
        elif init_base == 10:
            target_number = dec_to_other_base (init_number, target_base)
    return target_number

def do_the_job (init_number, init_base, target_base):
    quit_or_continue = "continue"
    while quit_or_continue not in quit_responses:
        if is_in_selected_base (init_number, init_base) == True:
            target_number = nbr_base_to_nbr_base (init_number, init_base, target_base)
            target_number = beauty_print (init_number, init_base, target_base, target_number)
            print( target_number ) 
        elif is_in_selected_base (init_number, init_base) == "not a base":
           print ( "Cette base n'est pas supportée dans le programme" )
        elif is_in_selected_base (init_number, init_base) == "not in selected base":
           print ( "Le nombre n'existe pas dans cette base" )
        quit_or_continue = str(input("souhaitez vous continuer ? : "))
    return "end of program"

do_the_job (ask_for_the_init_number, ask_for_the_init_base, ask_for_the_target_base)