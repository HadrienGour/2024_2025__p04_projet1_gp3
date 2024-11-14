ask_for_the_init_number = str(input("entrez le nombre initial :"))
ask_for_the_init_base = int(input("entrez la base de ce nombre (2, 10, 16) :"))
ask_for_the_target_base = int(input("entrez la base dans laquelle vous souhaitez passer ce nombre (2, 10, 16) :"))

bin_valid_chars = ["0", "1"]
dec_valid_chars = bin_valid_chars + ["2", "3", "4", "5", "6", "7", "8", "9"]
hex_valid_chars = dec_valid_chars + ["A", "B", "C", "D", "E", "F"]

base_error = "Cette base n'est pas supportée dans le programme"
number_error = "Ce nombre n'existe pas dans cette base"

quit_responses = ["non", "Non", "NON", "nan", "Nan", "NAN", "NON!", "No", "NO", "no", "quit", "Quit",\
                   "QUIT", "QUIT!", "exit", "Exit", "EXIT", "EXIT!", "sortir", "Sortir", "SORTIR", "sort",\
                      "Sort", "SORT", "n", "N", "quitter", "QUITTER", "QUITTER!", "quitter!", "stop", "STOP",\
                          "stop!", "STOP!", "end", "END", "out", "OUT"]