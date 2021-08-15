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

    def maxArea_UsingSort(self, h, w, horizontalCuts, verticalCuts):
        hsize = len(horizontalCuts)
        vsize = len(verticalCuts)

        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHeight = max(horizontalCuts[0], h - horizontalCuts[hsize - 1])
        maxWidth = max(verticalCuts[0], w - verticalCuts[vsize - 1])
        
        for i in range(1, hsize):
            maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i-1])
        
        for i in range(1, vsize):
            maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i-1])
        
        area = maxHeight * maxWidth
        
        return area % (10 ** 9 + 7)
index = 0
for _input, expected_output in \
        [
            ((5, 4, [1, 2, 4], [1, 3]), 4),
            ((5, 4, [3, 1], [1]), 6),
            ((5, 4, [3], [3]), 9),
        ]:
    s = Solution()
    index += 1
    actual_output = s.maxArea_UsingSort(*_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
