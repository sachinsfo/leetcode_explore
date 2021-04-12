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

    def deepestLeavesSum_dfs(self, root: TreeNode) -> int:
        '''
        T: 30%
        S: 97%
        :param root: takes in a tree as input
        :return: sum of all leaves at maximum depth
        '''
        data = dict()
        height = -math.inf
        # Do a regular dfs, except capture depth at each recursion
        def dfs(tree, depth=0):
            nonlocal data, height

            if not tree:
                return

            # calculate sum of leaves at their corresponding depths
            if not tree.left and not tree.right:
                height = max(height, depth)
                data[depth] = data.setdefault(depth, 0) + tree.val

            dfs(tree.left, depth + 1)
            dfs(tree.right, depth + 1)

        dfs(root)
        return data[height]

