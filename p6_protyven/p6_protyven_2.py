
mail_index = { "Newfoundland" : "A",
"Nova Scotia" : "B",
"Prince Edward Island" : "C",
"New Brunswick" : "E",
"Quebec" : {"G", "H", "J"},
"Ontario" : {"K", "L", "M", "N", "P"},
"Manitoba" : "R",
"Saskatchewan" : "S",
"Alberta" : "T",
"British Columbia" : "V",
"Nunavut" : "X",
"Northwest Territories" : "X",
"Yukon" : "Y"}

index = input("Hello! Enter mail index of the addresse: ")
index = tuple(i.upper() for i in index)

if len(index) !=  3: 
    print ("Incorrect index value")
else:
    if index[1].isdigit() and index[-1].isalpha() and index[-1].isascii():
        print ("The addressee is", end = ' ')
        if index[1] == "0":
            print ("in the countryside of the", end = ' ')
        else:
            print ("in an urban area of the", end = ' ')      

        if index[0] not in {"D", "F", "I", "O", "Q", "U", "W", "Z", "X", "K", "L", "M", "N", "P", "G", "H", "J"}:
            for city, letter in mail_index.items():
                if index[0] == letter:
                    print (city, " province")
# Робимо перевірку на ці індекси, тому що програма не считує в блоці 29-32 та нічого не видає(Х - окремий випадок)
        elif index[0] == "X" in mail_index.values():
                print ("Nunavut province or Northwest Territories")  
        elif index [0] in {"K", "L", "M", "N", "P"}:
            print ("Ontario province")
        elif index [0] in {"G", "H", "J"}:
            print ("Quebec province")
        else:
            print ("Incorrect index value")

    else: 
        print ("Incorrect index value")        