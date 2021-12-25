def check(x):
    try:
        int(x)
        if int(x)%16 == 0 and int(x)>0 and int(x)<1281:
            return True
        else:
            if int(x)<0:
                print("This number below 0!")
            elif int(x)>1280:
                print("Too high amount of pages.")
            else:
                if int(x)<16:
                    print(f"This value isn't multiple of 16. Try {int(x)-int(x)%16+16}.")
                else:
                    print(f"This value isn't multiple of 16. Try {int(x)-int(x)%16} or {int(x)-int(x)%16+16}.")
            return False
    except ValueError:
        print("Uncorrect value.")
        return False

def dec(active=True):
    def wrap(func):
        def wrapper(numb):
            if active:
                x = func(numb)
                l, lis = [], []
                for i in range(len(x)):
                    x_ = x[i]
                    l.append(tuple(x_[:4]))
                    l.append(tuple(x_[4:8]))
                    l.append(tuple(x_[8:12]))
                    l.append(tuple(x_[12:16]))
                    lis.append(l)
                    l = []
                print(f"Number of notebooks: {len(x)}.")
                for i in range(len(x)):
                    print(*lis[i])
            else:
                lis = func(numb)
                print(f"Number of notebooks: {len(lis)}.")
                for i in range(len(lis)):
                    print(lis[i])
        return wrapper
    return wrap

#If you want to highlight every 4 page numbers: @dec(active = True) or @dec(), else - @dec(active = False)
@dec(active=False)        
def list_(numb):
    lis = []
    numbers = [int(i) for i in range(1,numb+1)]
    for i in range(numb//16):
        m = []
        m.append(numbers[15])
        count,j, k  = 0 , 0, 0
        while k<4:
            if count == 0:
                m.append(numbers[j]) 
                m.append(numbers[j+1])
                count += 1
                j+= 1
                k += 1
            elif count == 1:
                m.append (numbers[15-j])
                m.append(numbers[14-j])
                j += 1
                count = 0
        m.append(numbers[8])
        lis.append(m)
        del numbers[0:16]
    return lis

while True:
    pages = input("Please enter amount of pages: ")
    if check(pages):
        pages = int(pages)
        break
list_(pages)
