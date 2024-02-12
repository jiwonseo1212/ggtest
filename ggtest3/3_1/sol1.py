import numpy as np


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
    x = np.array([1] + [0] * (len(m)-1))
    m = np.array([[i/sum(row) if sum(row) != 0 else 0 for i in row ] for row in m ])
    m = m.T
    print(m)
    total = np.zeros((1, len(m)))
    for i in range(40):
        x = np.matmul(m, x)
        total += x
    
    P = m
    I = np.eye(len(m))
    print(I)
    PI_diff = P - I
    print(PI_diff)
    U, S, Vt = np.linalg.svd(PI_diff)

    tolerance = 1e-5
    null_mask = (S <= tolerance)
    null_space = Vt.T[:, null_mask]
    print(null_space)
    print("stable state:")
    print(total)



def solution(m):

    test_make_stable_mat(m)




if __name__ == "__main__":
    testcase_m1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
    testcase_m2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    solution(testcase_m2)
    #assert solution(testcase_m1) == [7, 6, 8, 21]
     #assert solution(testcase_m2) == [0, 3, 2, 9, 14]
