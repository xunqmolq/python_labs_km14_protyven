def check_years(years):
    try:
        for i in years:
            int(i)
            if int(i) < 1:
                print("It's unreal")
                return False 
        return True
    except ValueError:
        print ("Uncorrect value. Enter again.")
        return False

def leap_year(i):
        i = int(i)
        if i%400 == 0:    
            return i
        elif i%4 == 0 and i%100 !=0:
            return i
        else:
            return 0

def check_month(x):
    try:
        int(x)
        x = int(x)
        if 1 <= x and x <=12:
            return True
        else:
            print ("It's unreal.")
            return False
    except ValueError:
        print ("Try again.")
        return False
        
def check_year(x):
    try:
        int(x)
        if len(x) == 4:
            return True
        else:
            print("Uncorrect.")
            return False 
    except Exception:
        print("Try again.")
        return False      

while True:
    years = input("Enter years separated by a space:").split()
    if check_years(years):
        break

leap = list(map(leap_year, years))
leap = [elem for elem in leap if elem]
print ("Leap years:", leap)

def amount_days (func):
    while True:
        month = input("Enter the month you are interested in: ")
        if check_month(month):
            month = int(month)
            break
    while True:
        year = input ("Enter the year(999 - 10000) you are interested in: ")
        if check_year(year):
            break
    day_30 = [4,6,9,11]
    day_31 = [1,3,5,7,8,10,11]
    day_29 = func(year)
    if month in day_30:
        print ("In this month 30 days")
    elif month in day_31:
        print  ("In this month 31 days")
    elif month == 2 and day_29 != 0:
        print  ("In this month 29 days")
    elif month == 2:
        print  ("In this month 28 days")
amount_days(leap_year)