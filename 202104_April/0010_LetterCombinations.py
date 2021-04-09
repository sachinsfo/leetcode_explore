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

    def letterCombinations(self, digits: str) -> List[str]:
        '''
        T: O(4**N) Beats 95%
        S: O(N)
        :param digits: str
        :return: List[str]
        '''
        memo = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if not digits:
            return []

        if digits in memo:
            return list(memo[digits])

        def combo(digits, memo, perms):
            if len(digits) == 1:
                return list(memo[digits])
            result = []
            for d in memo[digits[0]]:
                result += [d + perm for perm in combo(digits[1:], memo, perms)]
            return perms + result

        return combo(digits, memo, [])



index = 0
for _input, expected_output in \
        [
            ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
            ("", []),
            ("2", ["a","b","c"]),
        ]:
    s = Solution()
    index += 1
    actual_output = s.letterCombinations(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
