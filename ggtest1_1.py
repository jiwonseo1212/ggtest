
import random
from ggtest1_1_sols.sol1 import solution
import numpy as np

# Define the mean and standard deviation of your normal distribution
mean = 50
std_dev = 15

random_ints = [int(round(np.random.normal(mean, std_dev))) for i in range(10000000)]
print(random_ints[:10])
print(solution(random_ints, 10))


