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

    def threeSumClosest(self, nums, target):
        def twoSumClosest(_nums, _target):
            n = len(_nums)
            if n < 2:
                return -1
            low_value = math.inf 
            result = None
            for i in range(n):
                for j in range(n):
                    if i != j:
                        v1 = _nums[i]
                        v2 = _nums[j]
                        _sum = v1 + v2
                        diff = abs(_target - _sum)
                        if diff <= low_value:
                            low_value = diff 
                            result = (v1, v2)
            return result
        
        ans = math.inf 
        for i in range(len(nums)):
            v = nums[i]
            output = twoSumClosest(nums[:i] + nums[i+1:], target - v)
            total = v + output[0] + output[1]
            ans = min(total, ans)
        return ans 
                
        
        
index = 0
for _input, expected_output in \
        [
            (([-1, 2, 1, 4], 1), 2),
            (([-1, 2, 1, -4], 1), 2),
            # (,),
            # (,),
        ]:
    s = Solution()
    index += 1
    try:
        actual_output = s.threeSumClosest(*_input)
        assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
    except Exception as e:
        print('tc{}: Exception occured: {}'.format(index, e))
        break
else:
    print('\n*** All tests passed successfully! ***')
