'''
Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

from typing import List
import math

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
    def longestValidParentheses_BruteForce(self, s: str) -> int:
        max_length = -math.inf

        def check(string):
            nonlocal max_length
            def isvalid(_str):
                balance = 0
                for c in _str:
                    if c == '(':
                        balance += 1
                    elif c == ')':
                        balance -= 1
                    if balance < 0:
                        return False
                return balance == 0
            n = len(s)
            for i in range(n):
                for j in range(i, n):
                    substr = string[i:j+1]
                    if isvalid(substr):
                        max_length = max(max_length, len(substr))
        check(s)
        return max_length if max_length != -math.inf else 0

    def longestValidParentheses_DP(self, s: str) -> int:
        '''
        T: O(N)
        S: O(N)
        '''
        if not s:
            return 0

        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + (dp[i-2] if i > 1 else 0)
                else:
                    if i > dp[i-1] and s[i-dp[i-1]-1] == '(':
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        return max(dp)

    def longestValidParentheses_Stack(self, s: str) -> int:
        '''
        T: O(N)
        S: O(N)
        '''
        max_ans = 0
        stack = [-1]
        for i in range(len(s)):
            ch = s[i]
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_ans = max(max_ans, i - stack[-1])
        return max_ans

    def longestValidParentheses_TwoPointer(self, s: str) -> int:
        '''
        T: O(N)
        S: O(N)
        '''
        max_length = 0

        n = len(s)
        left = right = 0
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, 2 * left)
            elif right > left:
                left = right = 0

        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left = right = 0

        return max_length



index = 0
for _input, expected_output in \
        [
            ("(()",2),
            (")()())",4),
            ("",0),
            ("(()",2),
            ("()()()()()()",12),
            ("))))((((",0),
            ("((((()))))(()()()()())",22),
            ("))))()",2),
            ("))))())",2),
        ]:
    s = Solution()
    index += 1
    # actual_output = s.longestValidParentheses_BruteForce(_input)
    # actual_output = s.longestValidParentheses_DP(_input)
    # actual_output = s.longestValidParentheses_Stack(_input)
    actual_output = s.longestValidParentheses_TwoPointer(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
