import sys
sys.path.append("/Users/seojiwon/workspace/ggtest")
from utils import algorithm_performance_decorator

@algorithm_performance_decorator
def solution(l, t):
    res = [-1,-1]

    n = len(l)

    for i in range(n):
        rem = t
        for j in range(i,n):
            if rem == 0:
                return [i,j-1]
            elif rem < 0:
                break

            rem -= l[j]

    return res
