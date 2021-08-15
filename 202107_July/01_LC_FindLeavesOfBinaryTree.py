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
    def __init__(self):
        pass

    def findLeaves(self, root):
        def dfs(tree):
            if not tree:
                return
            print(tree.val)
            dfs(tree.left)
            dfs(tree.right)
        dfs(root)
        
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5

s = Solution()
s.findLeaves(t1)
