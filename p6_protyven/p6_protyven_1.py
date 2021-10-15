
phrase1 = input("Enter the first phrase: ").split()
phrase2 = input ("Enter the second phrase: ").split()
phrase1 = str(phrase1).lower()
phrase2 = str(phrase2).lower()

symbols1 = {item1 for item1 in phrase1 if item1.isalpha() }
symbols2 = {item2 for item2 in phrase2 if item2.isalpha() }

print ("Letters in the first phrase:", symbols1)
print ("Letters in the second phrase:", symbols2)
if symbols2 & symbols1 == symbols2:
    print ("Yes, we can create second phrase  letters from first phrase")
else: 
    print ("NO, we can't create second phrase  letters from first phrase")



