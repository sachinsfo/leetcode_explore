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

    def longestConsecutive_brute_force(self, nums):
        ''' TLE '''
        if not nums:
            return 0
        longest = -math.inf
        for num in nums:
            l = 0
            n = num
            while n in nums:
                l += 1
                longest = max(longest, l)
                n += 1
        return longest
    
    def longestConsecutive_sort(self, nums):
        if not nums:
            return 0
        
        longest = -math.inf
        nums = sorted(nums)
        for i in range(len(nums)-1):
            num = nums[i]
            l = 1
            j = i
            while j+1 < len(nums) and nums[j+1] == num + 1:
                l += 1
                longest = max(l, longest)
                num += 1
                j += 1
        return longest
        
index = 0
for _input, expected_output in \
        [
            ([100,4,200,1,3,2], 4),
            ([0,3,7,2,5,8,4,6,0,1], 9),
            # (,),
        ]:
    index += 1

    s = Solution()
    actual_output = s.longestConsecutive_brute_force(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)

    s = Solution()
    actual_output = s.longestConsecutive_sort(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)

    s = Solution()
    actual_output = s.longestConsecutive_brute_force(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
