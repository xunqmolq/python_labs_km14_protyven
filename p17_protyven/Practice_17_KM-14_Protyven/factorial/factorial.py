def fact(i):
    if i == 1:
        return 1
    else:
        result = i * fact(i-1)
        return result