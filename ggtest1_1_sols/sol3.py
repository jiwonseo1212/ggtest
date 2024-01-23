
"""
-- Python cases --

Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n) would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.   

Input:
solution.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
Output:
    1,4
"""

from collections import defaultdict
from utils import algorithm_performance_decorator


@algorithm_performance_decorator
def solution2(data, n):
    integer_dict = defaultdict(int)

    for num in data:
        integer_dict[num] +=1 

    new_list = [d for d in data if integer_dict[d] <= n ] 

    return new_list

