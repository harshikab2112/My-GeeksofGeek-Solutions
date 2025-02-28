def alphabets(c1,c2):
    #Code below to print alphabets from c1 to c2
    # Don't provide a new line after printing
    for i in range(ord(c1),ord(c2)+1): #ord() - Converts/returns the ASCII (or Unicode) value of a character
        print(chr(i),end=" ") #converts an ASCII value back into a character
