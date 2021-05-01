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

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_sum = math.inf
        n = len(triangle)
        memo = dict()
        def get_minimum(index, path_sum, depth):
            nonlocal min_sum, triangle, n, memo

            if (depth, index) in memo:
                return memo[(depth, index)]

            if depth == n:
                return path_sum

            for i in [index, index + 1]:
                val = triangle[depth][i]
                min_value = get_minimum(i, path_sum + val, depth + 1)
                min_sum = min(min_sum, min_value)
            memo[(depth, index)] = min_sum
            return min_sum


        get_minimum(0, triangle[0][0], 1)
        # print(memo)
        return min_sum if min_sum != math.inf else triangle[0][0]


index = 0
for _input, expected_output in \
        [
            # ([[2],[3,4],[6,5,7],[4,1,8,3]], 11),
            # ([[-10]], -10),
            ([[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]], -63),
        ]:
    s = Solution()
    index += 1
    actual_output = s.minimumTotal(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
