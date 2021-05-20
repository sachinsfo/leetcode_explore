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
        self.min_moves = math.inf
        self.x = 0
        self.y = 0

    def minKnightMoves(self, x: int, y: int) -> int:
        self.x = x
        self.y = y
        def minimum(x, y, visited=set(), moves=0):
            if x == self.x and y == self.y:
                return moves

            if abs(x) > self.x * 2 or abs(y) > self.y * 2:
                return math.inf

            for direction in [
                (2, 1), (2, -1),
                (-2, 1), (-2, -1),
                (1, 2), (1, -2),
                (-1, 2), (-1, -2)
            ]:
                next_point =  (x + direction[0], y + direction[1])
                if next_point not in visited:
                    # print(next_point)
                    visited.add(next_point)
                    result = minimum(next_point[0], next_point[1], visited, moves+1)
                    self.min_moves = min(self.min_moves, result)
                return self.min_moves
        minimum(0, 0)
        return self.min_moves


index = 0
for _input, expected_output in \
        [
            ((5, 5), 4),
            ((2, 1), 1),
            # (,),
        ]:
    s = Solution()
    index += 1
    actual_output = s.minKnightMoves(*_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
