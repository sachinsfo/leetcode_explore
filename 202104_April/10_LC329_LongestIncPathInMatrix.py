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

    def longestIncreasingPathInMatrix_naive_dfs(self, matrix):
        pass

    def longestIncreasingPathInMatrix_memoization(self, matrix):
        # https://www.youtube.com/watch?v=uLjO2LUlLN4

        # instead of adding and subtracting each time to
        # compute new set of directions, we use this list
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols, longest_path = len(matrix), len(matrix[0]), 0
        dp = [[0 for x in range(cols)] for y in range(rows)]

        def longestIncreasingPath(matrix, rows, cols, r, c):
            nonlocal directions, dp
            if dp[r][c] > 0: return dp[r][c]
            max_len = 0
            for direction in directions:
                new_r = direction[0] + r
                new_c = direction[1] + c
                # making sure this new point is a valid point
                if new_r > -1 and new_c > -1 and new_r < rows and new_c < cols and \
                    matrix[new_r][new_c] > matrix[r][c]:
                    longest = longestIncreasingPath(matrix, rows, cols, new_r, new_c)
                    max_len = max(max_len, longest)
            dp[r][c] = max_len + 1
            return dp[r][c]

        if not matrix or len(matrix) == 0:
            return 0


        for r in range(rows):
            for c in range(cols):
                longest = longestIncreasingPath(matrix, rows, cols, r, c)
                longest_path = max(longest_path, longest)
        return longest_path

index = 0
for _input, expected_output in \
        [
            ([[1, 2]], 2),
            ([[9,9,4],[6,6,8],[2,1,1]], 4),
            ([[3,4,5],[3,2,6],[2,2,1]], 4),
            ([[1]], 1),
        ]:
    s = Solution()
    index += 1
    # actual_output = s.longestIncreasingPathInMatrix_naive_dfs(_input)
    actual_output = s.longestIncreasingPathInMatrix_memoization(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
