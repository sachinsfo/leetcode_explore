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
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        output = set()
        x_limit = math.log(bound, x) if x not in (0, 1) else 1
        y_limit = math.log(bound, y) if y not in (0, 1) else 1
        # print(x_limit, y_limit)
        for i in range(int(x_limit)+1):
            for j in range(int(y_limit)+1):
                val = x ** i + y ** j
                if val <= bound:
                    output.add(val)
        return list(output)


index = 0
for _input, expected_output in \
        [
            ((2, 1, 10),[9,2,3,5]),
            ((2, 3, 10),[2,3,4,5,7,9,10]),
            # (,),
        ]:
    s = Solution()
    index += 1
    actual_output = s.powerfulIntegers(*_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
