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

    def minMoves2_bruteForce(self, nums):
        ans = math.inf
        min_val = min(nums)
        max_val = max(nums)
        '''
        There must be a value between min_val and max_val
        for which the total of abs(difference with all elements in the array) is minimum
        '''
        for i in range(min_val, max_val + 1):
            total = 0
            for n in nums:
                total += abs(n - i)
            ans = min(ans, total)
        return ans
        
        
index = 0
for _input, expected_output in \
        [
            ([1, 2, 3], 2),
            ([1, 10, 2, 9], 16),
            # (,),
        ]:
    s = Solution()
    index += 1
    actual_output = s.minMoves2_bruteForce(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')