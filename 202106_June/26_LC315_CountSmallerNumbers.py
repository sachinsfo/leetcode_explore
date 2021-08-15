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

    def countSmaller(self, nums):
        output = []
        n = len(nums)
        for i in range(n):
            j = i + 1
            if j < n:
                counter = 0
                value = nums[i]
                while j < n:
                    if nums[j] < value: 
                        counter += 1
                    j += 1
                output.append(counter)
        output.append(0)
        return output
        
        
index = 0
for _input, expected_output in \
        [
            ([5, 2, 6, 1], [2, 1, 1, 0]),
            ([-1], [0]),
            ([-1, -1], [0, 0]),
        ]:
    s = Solution()
    index += 1
    actual_output = s.countSmaller(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
