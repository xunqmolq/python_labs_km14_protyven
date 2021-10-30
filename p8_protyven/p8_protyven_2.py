import math
print ("a(x**2)+b*x+c=0")

def check(n):
    try:
        float(n)
        return True
    except ValueError:
        print ("Wrong value. Try agian.")
        return False

while True:
    a = (input ("Enter a: "))
    if check (a):
        a = float(a)
        break
while True:
    b = (input ("Enter b: "))
    if check (b):
        b = float(b)
        break

while True:
    c = (input ("Enter c: "))
    if check (c):
        c = float(c)
        break

x1 = float()
x2 = float()
D =(b)**2 - 4*a*c

if D > 0:
    try:
        x1 = (-b+math.sqrt(D))/(2*a)
        x2 = (-b-math.sqrt(D))/(2*a)
        print ("Your equation roots: ",round(x1,4),",", round(x2,4))
    except ZeroDivisionError:
        try:
            x1 = -c/b
            print ("Your equation roots: ", round(x1,4))
        except ZeroDivisionError:
            print ("Oh no...Problem: division by zero")

elif D == 0:
    try:
        x1 = (-b)/(2*a)
        print ("Your equation roots: x1 = x2", round(x1,4))
    except ZeroDivisionError:
        print ("Oh no...Problem: division by zero")

try:    
    if D < 0:
        raise ValueError ("Discriminant less then zero. There are no roots of the equation.")
except ValueError as val_er:
    print (val_er)