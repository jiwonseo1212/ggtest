
import sys
from collections import deque

sys.path.append("/Users/seojiwon/workspace/ggtest")
from utils import algorithm_performance_decorator

@algorithm_performance_decorator
def solution(l, t):
    # reall = l[:]
    l = deque(l)
    queue = deque()
    queue_sum = 0
    pop_ind = 0
    while queue or l:
        # queue_sum < t: add queue new elem if elem while queue_sum < t
        while queue_sum < t and l:
            elem = l.popleft()
            queue.append(elem)
            queue_sum += elem

        # queue_sum > t: pop queue old elem if queue while queue_sum > t
        while queue_sum > t and queue:
            popped = queue.popleft()
            queue_sum -= popped
            pop_ind += 1
        
        if queue_sum < t and not l: #if thers is no possibilty for solve
            return [-1, -1]
        
        if queue_sum == t: #exit!
            return [pop_ind, pop_ind + len(queue) - 1]

    return [-1, -1]

