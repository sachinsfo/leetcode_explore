# @Author  : github.com/sachinsfo

from typing import List
import math
from heapq import heappush as hpush
from heapq import heappop as hpop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass

    def minCost_recursion(self, costs):

        def paint_cost(i, color):
            total_cost = costs[i][color]

            if i == len(costs)-1:
                pass
            elif color == 0:
                total_cost += min(paint_cost(i+1, 1), paint_cost(i+1, 2))
            elif color == 1:
                total_cost += min(paint_cost(i+1, 0), paint_cost(i+1, 2))
            elif color == 2:
                total_cost += min(paint_cost(i+1, 0), paint_cost(i+1, 1))
            
            return total_cost

        if not costs:
            return 0
        
        return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
        
        
index = 0
for _input, expected_output in \
        [
            ([[17,2,17],[16,16,5],[14,3,19]], 10),
            ([[7,6,2]], 2),
        ]:
    s = Solution()
    index += 1
    actual_output = s.minCost_recursion(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)

    actual_output = s.minCost_recursion(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
