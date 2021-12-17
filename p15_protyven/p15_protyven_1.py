def check_int(x):
    try:
        int(x)
        if int(x)>0:
            return True
        else:
            print("This value below zero!")
            return False
    except ValueError:
        print("Uncorrect value")
        return False

while True:
    n = input("Enter degree of binomial Newton's: ")
    if check_int(n):
        n = int(n)
        break

pascal = [1]
for i in range(n+1):
    print(*pascal)
    pascal = [sum(x) for x in zip([0]+pascal, pascal+[0])]

