def is_in_base (number, base):
    if base == 2:
        bin_valid_chars = ["0", "1"]
    elif base == 10:
        dec_valid_chars = bin_valid_chars + ["2", "3", "4", "5", "6", "7", "8", "9"]
    elif base == 16:
        hex_valid_chars = dec_valid_chars + ["A", "B", "C", "D", "E", "F", "a", "b", "c", "d", "e", "f"]
        valid_chars
    else:
        print ("Cette base n'est pas supportée dans le programme")
    
    
    for j in number:
        if j in valid_chars:
            pass
        else:
            print ("Le nombre n'existe pas dans cette base")
            return False
    return True

print (is_in_base(145, 10))


# def dec_to_bin (n):
#     k=[]
#     while n != 0:
        
#         n = n//2
#     return str(k)

# print(dec_to_bin(5))