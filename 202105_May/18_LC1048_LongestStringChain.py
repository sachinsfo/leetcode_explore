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
    """
    https://www.youtube.com/watch?v=pXG3uE_KqZM
    Time: O(N logN) + O(N * L * L)
    Space: O(NL) or O(N)
    """
    def __init__(self):
        pass
    def longestStringChain_recursive(self, words):
        # O(N log N)
        words.sort(key=lambda x: len(x))
        res = 0
        memo = dict()
        # O(N)
        for word in words:
            memo[word] = memo.setdefault(word, 1)
            # O(L * L)
            for i in range(len(word)):
                curr = word[:i] + word[i+1:]
                if curr in memo:
                    memo[word] = max(memo[word], memo[curr]+1)
            res = max(res, memo[word])
        return res
    
    def topdown_dp(self, words):
        wordsPresent = set(words)
        memo = dict()

        def dfs(curr, wordsPresent):
            nonlocal memo 
            if curr in memo:
                return memo[curr]
            max_len = 1
            for i in range(len(curr)):
                new_word = curr[:i] + curr[i+1:]
                if new_word in wordsPresent:
                    curr_len = 1 + dfs(new_word, wordsPresent)
                    max_len = max(max_len, curr_len)
            memo[curr] = max_len
            return memo[curr]

        ans = 0
        for word in words:
            ans = max(ans, dfs(word, wordsPresent))
        return ans

        
        
index = 0
for _input, expected_output in \
        [
            (["a","b","ba","bca","bda","bdca"],4),
            (["xbc","pcxbcf","xb","cxbc","pcxbc"],5),
            # ([],[]),
        ]:
    s = Solution()
    index += 1
    actual_output = s.longestStringChain_recursive(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
    actual_output = s.topdown_dp(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')