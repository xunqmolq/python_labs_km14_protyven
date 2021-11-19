import copy
def cons (head, tail = []):
    lst = []
    lst.append(head)
    lst.extend(tail)
    return lst
l = cons(3, 
        cons(2, 
            cons(1, [])))
print(f'Result: {l}')

assert l == [3, 2, 1], 'Failed test 1'
assert cons(1) == [1], 'Failed test 2'
print('All tests good!')


def sum(l, accumulator = 0):
    if l == []:
        return accumulator
    else:
        accumulator = accumulator + l[-1]
        del l[-1]
        return sum(l, accumulator)

print("Sum = ", sum(copy.copy(l)))
assert sum(l) == 6, 'Failed on sum'
print('All tests good!')
