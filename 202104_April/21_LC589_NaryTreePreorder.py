from typing import List
import math
from heapq import heappush as hpush
from heapq import heappop as hpop

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        pass

    def NAryTreePreorderTraversal(self, root):
        output = []
        stack = []
        while stack:
            node = stack.pop()
            if not node:
                continue

            output.append(node.val)
            stack.extend(node.children[::-1])

        return output


