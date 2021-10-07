words = input("Enter words through space: ").split()
if len (words)>=3:
    print (', '.join(words[:len(words)-1]), end=" " )
    print ("and ", words[-1])
elif len (words) == 1:
    print (words)
elif len (words) == 2:
    print (words[0], "and ", words[1])
else: 
    print ("Error. Try again")
