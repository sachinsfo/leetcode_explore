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

    def candy(self, ratings):
        pass
        
        
index = 0
for _input, expected_output in \
        [
            ([1, 0, 2], 5),
            ([1, 2, 2], 4),
        ]:
    s = Solution()
    index += 1
    actual_output = s.candy(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
