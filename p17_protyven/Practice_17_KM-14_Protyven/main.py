from exp_root.exponentation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, ln, lg

def check(x, func):
    try:
        float(x)
        if func == "lg" or func == "ln" or func == "log":
            if float(x) > 0:
                return True
            else:
                print("Number less than zero")
                return False
        elif func == "root2" or func == "root3":
            if float(x)>0:
                return True
            else:
                print("Number less than zero")
                return False
        elif func == "factorial":
            try:
                int(x)
                if int(x)>0:
                    return True
                else:
                    print("Number less than zero")
                    return False
            except ValueError:
                print("Enter a natural number!")
                return False
        else:
            return True
    except ValueError:
        print("Enter a number!")
        return False


def main():
    func = input("Enter what you want to do(exponentiation2, exponentiation3, root2, root3, factorial, log, lg, ln): ")
    if func == "log":
        while True:
            a = input("Enter base: ")
            def check_a(a):
                try:
                    float(a)
                    if float(a)>0 and float(a)!=1:
                        return True
                    else:
                        print("Incorrect value")
                except ValueError:
                    print("Incorrect value")
                    return False
            if check_a(a):
                a = float(a)
                break
            else:
                print("Incorrect value")
        while True:
            numb = input("Please enter a number greater than 0: ")
            if check(numb,func):
                print(f"Result: {log(a, float(numb))}")
                break
            else:
                print("Incorrect value")

    elif func == "root2":
        while True:
            numb = input("Please enter a number greater than 0: ")
            if check(numb, func):
                print(f"Result: {root2(float(numb))}")
                break
            else:
                print("Incorrect value")
    elif func == "root3":
        while True:
            numb = input("Please enter a number greater than 0: ")
            if check(numb, func):
                print(f"Result: {root3(float(numb))}")
                break
            else:
                print("Incorrect value")
    elif func =="factorial":
        while True:
            numb = input("Please enter a natural number: ")
            if check(numb, func):
                print(f"Result: {fact(int(numb))}")
                break
            else:
                print("Incorrect value")
    elif func == "lg":
        while True:
            numb = input("Please enter a number greater than 0: ")
            if check(numb, func):
                print(f"Result: {lg(float(numb))}")
                break
            else:
                print("Incorrect value")
    elif func == "ln":
        while True:
            numb = input("Please enter a number greater than 0: ")
            if check(numb, func):
                print(f"Result: {ln(float(numb))}")
                break
            else:
                print("Incorrect value")

    elif func == "exponentiation2":
        while True:
            numb = input("Enter any number: ")
            if check(numb, func):
                print(f"Result{exp2(float(numb))}")
                break
            else:
                print("Incorrect value")

    elif func == "exponentiation3":
        while True:
            numb = input("Enter any number: ")
            if check(numb, func):
                print(f"Result: {exp3(float(numb))}")
                break
            else:
                print("Incorrect value")
    else:
        print("Unknown function!")

if __name__ == '__main__':
    main()

