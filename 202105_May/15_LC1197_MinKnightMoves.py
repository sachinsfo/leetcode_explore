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
    def _(self):
        pass
        
        
index = 0
for _input, expected_output in \
        [
            (,),
            (,),
            (,),
        ]:
    s = Solution()
    index += 1
    actual_output = s.(*_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')