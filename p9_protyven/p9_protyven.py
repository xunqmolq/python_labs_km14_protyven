
import numpy as np
import itertools

def check_int(x):
    """
    This function checks the entered value for belonging to the type of integers.
    """
    try:
        int(x)
        return True
    except ValueError:
        print ("Oh no...Incorrect value. Try again")
        return False

def random_matrix(size):
    """
    The function generates dim x dim array of integers
    between 0 and 20.
    """
    matrix = np.random.randint(20, size = (size, size))
    return matrix

def sign(x):
    """
    This function determines the sign before the term.
    """
    q = -1
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i] > x[j]:
                q = -1*q
    return q

def permutation(size):
    """
    This function performs a permutation on the range of the dimension of the matrix.
    """
    perm = []
    for i in range (size):
        perm.append(i)
    perm = list(itertools.permutations(perm, size))
    return perm

def multiplication(sign, size, matrix):
    """
    This function multiplies the elements of the matrix.
    """
    multip = 1
    for i in range(size):
        multip *= matrix[i][int(sign[i])-1]
    return multip

def summ(size, matrix):
    """
    This function performs addition of terms.
    """
    sum = 0
    for i in permutation(size):
        sum += sign(i)*multiplication(i, size, matrix)
    return sum

while True:
    size_matr = input("Enter NxN matrix's size, N = ")
    if check_int(size_matr):
        size_matr = int(size_matr)
        break

matrix = random_matrix(size_matr)
print("Your Matrix:\n", matrix)
det = summ(size_matr, matrix)
print("Your determinant =", det)