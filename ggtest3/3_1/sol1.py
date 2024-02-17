import math
from fractions import Fraction

def matmul_fraction(A, B):
    result = [[Fraction(0) for _ in range(len(B[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def test_make_stable_mat(m):
    """
    [
    [0,1,0,0,0,1], # s0, the initial state, goes to s1 and s5 with equal probability
    [4,0,0,3,2,0], # s1 can become s0, s3, or s4, but with different probabilities
    [0,0,0,0,0,0], # s2 is terminal, and unreachable (never observed in practice)
    [0,0,0,0,0,0], # s3 is terminal
    [0,0,0,0,0,0], # s4 is terminal
    [0,0,0,0,0,0], # s5 is terminal
    ]
    """
    x = [[Fraction(1)] + [Fraction(0)] * (len(m)-1)]
    m = [[Fraction(i, sum(row)) if sum(row) != 0 else Fraction(0) for i in row ] for row in m ]
    # m = m.T
    # print(m)
    
    total = [Fraction(0) * len(m)]
    for i in range(40):
        x = matmul_fraction(m, x)
        # total += x
    
    print(x)
    # P = m
    # I = np.eye(len(m))
    # print(I)
    # PI_diff = P - I
    # print(PI_diff)
    # U, S, Vt = np.linalg.svd(PI_diff)

    # tolerance = 1e-5
    # null_mask = (S <= tolerance)
    # null_space = Vt.T[:, null_mask]
    # print(null_space)
    # print("stable state:")
    # print(total)



def solution(m):
    total = [[Fraction(0)]* len(m)]
    x = [[Fraction(1)] + [Fraction(0)] * (len(m)-1)]
    mm = [[Fraction(i, sum(row)) if sum(row) != 0 else Fraction(0) for i in row ] for row in m ]
    len([bool(sum(elem)) for elem in m])
    for i, row in enumerate(m):
        # for j, elem in enumerate(row):
        #     if elem != 0:
        if sum(row): # if the row is non-terminal:
            row
    # for _ in range(len(m)):
    #     x = matmul_fraction(x, mm)
    #     for i in range(len(total[0])):
    #         total[0][i] += x[0][i]
        


    nums = [frac.numerator for frac in total[0]]
    denoms = [frac.denominator for frac in total[0]]
    lcm = math.lcm(*denoms)
    numx = list(map(lambda x: lcm//x, denoms))
    print(total)




if __name__ == "__main__":
    testcase_m1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
    testcase_m2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    solution(testcase_m1)
    #assert solution(testcase_m1) == [7, 6, 8, 21]
     #assert solution(testcase_m2) == [0, 3, 2, 9, 14]
