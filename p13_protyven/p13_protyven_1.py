from collections import Counter
import os
import re

x = os.path.abspath(__file__).replace("\\p13_protyven_1.py", "")
os.chdir(x)

inFile = open("gadsby.txt", "r")
text = str(inFile.readlines())
text = ''.join(sorted((re.sub("[^A-Za-z]", "", text).lower())))
count = len(text)
dictionary = dict(Counter(text))
max_number=max(dictionary.values())
keys_max =[]
dict_max = dict(dictionary)
key_min = []
dict_min = dict(dictionary)
for i in range(5):
    max_number=max(dict_max.values())
    min_number=min(dict_min.values())
    for key, value in dict(dict_max).items():
        if value == max_number:
            keys_max.append(dict_max[key])
            del dict_max[key]
    for key, value in dict(dict_min).items():
        if value == min_number:
            key_min.append(dict_min[key])
            del dict_min[key]
            
for key,value in dictionary.items():
    print("Letter",key,"have",value,"occurrences. Percentage =", round((value/count)*100, 3))
print("\n5 most common letters :")
for key,value in sorted(dictionary.items(), key = lambda x: x[1], reverse= True):
    if key not in dict_max:
        print(key,"meets", value, "times. Percentage =", round((value/count)*100, 3))
print("5 least common letters :")
for key,value in sorted(dictionary.items(), key = lambda x: x[1], reverse = True):
    if key not in dict_min:
        print(key,"meets", value, "times. Percentage =", round((value/count)*100, 3))