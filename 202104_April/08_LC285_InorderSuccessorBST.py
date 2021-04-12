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
        # previous, inorder successor
        self.prev = None
        self.succ = None

    def inorderSuccessorBinaryTree(self, root: TreeNode, p: TreeNode):
        prev, succ = None, None
        def inorder(root, p):
            pass
        '''TBD'''

    def inorderSuccessorBST_slow(self, root: TreeNode, p:TreeNode) -> TreeNode:
        '''
        T: O(N)
        S: O(N)
        '''
        minimal = math.inf
        ans = None

        def dfs(tree, p):
            nonlocal ans, minimal
            if not tree:
                return

            value = tree.val - p.val
            if tree.val > p.val and value < minimal:
                ans = TreeNode(tree.val, tree.left, tree.right)
                minimal = value

            dfs(tree.left, p)
            dfs(tree.right, p)

        dfs(root, p)
        return ans

    def inorderSuccessor_fast(self, root: TreeNode, p: TreeNode):
        '''
        T: O(N) - Worst case in skewed tree
        S: O(1)
        '''
        successor = None

        while root:

            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor

