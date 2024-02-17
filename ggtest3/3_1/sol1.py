from functools import reduce
from fractions import Fraction
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def _lcm(a, b):
    return a * b // gcd(a, b)
def lcm(*args):
    return reduce(_lcm, args)
def matmul_fraction(A, B):
    result = [[Fraction(0) for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
def swap(i, ind, m):
    m[i], m[ind] = m[ind], m[i]
    for k in range(len(m)):
        m[k][i], m[k][ind] = m[k][ind], m[k][i]
def getim(matrix):
    rows = len(matrix)
    augmented = [row + [Fraction(int(i == j), 1) for i in range(rows)] for j, row in enumerate(matrix)]
    for r in range(rows):
        pivot = augmented[r][r]
        if pivot == 0:
            for k in range(r + 1, rows):
                if augmented[k][r] != 0:
                    augmented[r], augmented[k] = augmented[k], augmented[r]
                    pivot = augmented[r][r]
                    break
        for c in range(2*rows):
            augmented[r][c] /= pivot
        for i in range(rows):
            if i != r:
                factor = augmented[i][r]
                for c in range(2*rows):
                    augmented[i][c] -= factor * augmented[r][c]
    inverse_matrix = [row[rows:] for row in augmented]
    return inverse_matrix
def solution(m):
    n = len(m)
    if n==1:
        if len(m[0]) == 1 and m[0][0] == 0:
            return [1, 1]
    mm = [[Fraction(i, sum(row)) if sum(row) != 0 else Fraction(0) for i in row ] for row in m ]
    len([bool(sum(elem)) for elem in mm])
    for i, row in enumerate(mm):
        if sum(row): 
            ind = i-1 
            while i!=0 and (not sum(mm[ind])):
                swap(i, ind, mm)
                ind -= 1
                i-=1
    i = [sum(r) for r in mm].index(0)
    mat_QR = mm[:i]
    mat_Q, mat_R = [m[:i] for m in mat_QR], [m[i:] for m in mat_QR]
    I_Q= [[Fraction(1) - k if i == j else Fraction(0) - k for j, k in enumerate(m)] for i, m in enumerate(mat_Q)]
    I_Q_1 = getim(I_Q)
    Q_R = matmul_fraction(I_Q_1, mat_R)
    nums = [frac.numerator for frac in Q_R[0]]
    denoms = [frac.denominator for frac in Q_R[0]]
    lcmdenom = lcm(*denoms)
    numx = list(map(lambda x: lcmdenom//x, denoms))
    return [n*x for n, x in zip(nums, numx)] + [lcmdenom]




if __name__ == "__main__":
    testcase_m1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
    testcase_m2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    solution(testcase_m1)
    assert solution(testcase_m1) == [7, 6, 8, 21]
    assert solution(testcase_m2) == [0, 3, 2, 9, 14]


