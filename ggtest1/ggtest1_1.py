
import random
from ggtest1_1_sols.sol1 import solution
import numpy as np
from ggtest1_1_sols.sol2 import solution2
from ggtest1_1_sols.sol3 import solution2 as solution3

# Define the mean and standard deviation of your normal distribution
mean = 300
std_dev = 15

random_ints = [int(round(np.random.normal(mean, std_dev))) for i in range(10000000)]
print(random_ints[:10])
print(solution(random_ints, 10))
print(solution2(random_ints, 10))
print(solution3(random_ints, 10))



