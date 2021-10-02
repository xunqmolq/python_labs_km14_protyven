try:
    try:
        age = float(input ("Enter dog's age in calendar years: "))
        if age >= 2:
            dog_age = 20.5 + (age-2)*4
        elif age > 0 and age < 2:
            dog_age = age*10.5
        print ("Dog is", dog_age, " years old")
    except NameError:
        print ("Uncorrect value")
except ValueError:
    print ("Uncorrect value")

