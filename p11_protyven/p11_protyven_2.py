import copy

def rrange (begin, end, step = 1):
    if step == 0:
        return []
    elif begin > end and step >0:
        return []
    elif begin < end and step <0:
        return []
    else:
            if begin != end:
                l.append(begin)
                return rrange(begin+step, end, step)
            else:
                lst = copy.copy(l)
                return lst  
 #For new function call you need to make l = []               
l = []
x = rrange(1, 10)
l = []
y = rrange(10, 1, -1)
l = []
z = rrange(10, 1, 1)
print(x, y, z)

assert x == list(range(1, 10)), 'Failed test for simple range'
assert y == list(range(10, 1, -1)), 'Failed test for reverse range'
assert z == list(range(10, 1, 1)), 'Failed test for empty range'
print('All tests good!')
