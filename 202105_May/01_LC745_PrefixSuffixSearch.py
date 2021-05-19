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


class WordFilter:
    '''
    Time limit exceeded
    TBD: Use Trie for optimal solution
    '''
    def __init__(self, words: List[str]):
        # (x, y) : [0,1,2]
        self.cache = dict()
        self.words = words
        self.size = len(words)

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix, suffix) in self.cache:
            return self.cache[(prefix, suffix)][-1]
        for i in range(self.size):
            m = len(prefix)
            n = len(suffix)
            word = self.words[i]
            w = len(word)
            if m <= w and n <= w:
                p = word[:m]
                s = word[-n:]
                if p == prefix and s == suffix:
                    self.cache[(prefix, suffix)] = self.cache.setdefault((prefix, suffix), []) + [i]
        return self.cache[(prefix, suffix)][-1]

