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

    def minMoves2_brute_force(self, nums):
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
    
    def minMoves2_better_brute_force(self, nums):
        """
        Instead of search all the numbers between min and max of the array,
        By mathematical analysis we knew that the number must be in the array
        So we iterate twice on the array elements for each loop finding the
        minimum possible value
        """
        min_val = math.inf
        for num in nums:
            total = 0
            for n in nums:
                total += abs(n - num)
            min_val = min(min_val, total)
        return min_val
    
    def sorting_technique(self, nums):
        pass

    def median_sorting(self, nums):
        """
        Time - O(n log n) 
        Space - O(1)
        """
        total = 0
        median_index = len(nums)//2
        nums.sort()
        for num in nums:
            total += abs(nums[median_index] - num)
        return total
    
    def without_median(self, nums):
        """
        First we find the min and max
        and find num of moves to make them equal to some 'k'
        by calculating their difference
        Then at each loop we find the moves for next min and max & so on
        """
        low, high = 0, len(nums) - 1
        nums.sort()
        total = 0
        while low < high:
            total += nums[high] - nums[low]
            low += 1
            high -= 1
        return total
    
    def median_quick_sort(self, nums):
        pass
    
    def median_of_medians(self, nums):
        pass
        
index = 0
for _input, expected_output in \
        [
            ([1, 2, 3], 2),
            ([1, 10, 2, 9], 16),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25),
        ]:
    s = Solution()
    index += 1
    actual_output = s.minMoves2_brute_force(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
    actual_output = s.minMoves2_better_brute_force(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
    # actual_output = s.sorting_technique(_input)
    # assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
    actual_output = s.without_median(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')