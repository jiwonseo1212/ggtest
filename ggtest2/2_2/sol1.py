"""

Ion Flux Relabeling
===================
Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired spectacularly. The Commander had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. Commander Lambda is having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, Lambda performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

7
3 6
1 2 4 5

        15
   7         14
  3 6      10   13
1 2 4 5   8 9  11 12

Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter. For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(3, {7, 3, 5, 1})
Output:
    -1,7,6,3

Input:
Solution.solution(5, {19, 14, 28})
Output:
    21,15,29

-- Python cases --
Input:
solution.solution(5, [19, 14, 28])
Output:
    21,15,29

Input:
solution.solution(3, [7, 3, 5, 1])
Output:
    -1,7,6,3
"""
import sys
sys.path.append("/Users/seojiwon/workspace/ggtest")
from utils import algorithm_performance_decorator


class BTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def __str__(self) -> str:
        return str(self.value)

class BTree:
    def __init__(self, height):
        self.btree_start_node = self.make_btree(height)
        print(self.btree_start_node)
    
    def print_node(self, node):
        print(f"{node}")
        if node.left and node.right:
            print("---------")
            self.print_node(node.left)
            self.print_node(node.right)
            print("===========")
            

    def make_node(self, value, height=0):
        """
            15
        7         14
        3 6      10  13
        1 2 4 5   8 9  11 12
                        
        """
        parent = BTreeNode(value)
        if height == 1:
             return parent
        right = value-1
        left = right - (pow(2, height-1)) -1 
        parent.left = self.make_node(left, height=height-1)
        parent.right = self.make_node(value-1, height=height-1)
        return parent

    def make_btree(self, height):
        value = pow(2, height)-1
        start_node = self.make_node(value, height=height)
        self.print_node(start_node)
        return start_node

    


@algorithm_performance_decorator
def solution(h, l):
    btree = BTree(h)



if __name__ == "__main__":
    solution(4, [7, 3, 5, 1])






     
# print(solution([2,2,2,2,2], 4))
# print(solution([1, 2, 3, 4], 15))
# print(solution([4, 3, 10, 2, 8], 12))
