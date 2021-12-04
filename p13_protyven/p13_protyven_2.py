
import os
from collections import Counter

x = os.path.abspath(__file__).replace("\\p13_protyven_2.py", "")
os.chdir(x)
file_list = (os.listdir('archive')[1:])
os.chdir(os.path.abspath(__file__).replace("\\p13_protyven_2.py", "\\archive\\"))

m,f = {}, {}
name_ = []
count =0
list_f = []
list_m = []
for i in file_list:    
    inFile = open(i,"r")
    names = list(inFile.readlines())
    m,f = {}, {}
    for j in names:
        j = j.replace("\n", '')
        (name, sex, times) = j.split(',')
        if sex == "F":
            f[name] = int(times)
        elif sex == "M":
            m[name] = int(times)
    max_f = max(f.values())
    max_m = max(m.values())
    for key,value in f.items():
        if value == max_f:
            list_f.append(key)
    for key,value in m.items():
        if value == max_m:
            list_m.append(key)
print("THE MOST COMMON MALE NAMES:\n")
for key,value in sorted(dict(Counter(list_m)).items(), key = lambda x: x[1], reverse=True):
    print(key, "was the most popular name", value, "times")
print("\nTHE MOST COMMON FEMALE NAMES:\n")
for key,value in sorted(dict(Counter(list_f)).items(), key = lambda x: x[1], reverse=True):
    print(key, "was the most popular name", value, "times")
