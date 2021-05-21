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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [root]
        output = []
        while q:
            size = len(q)
            local = []
            for i in range(size):
                node = q.pop(0)
                if node:
                    local.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if local:
                output.append(local)
        return output
        
n1 = TreeNode(1)        
n2 = TreeNode(2)        
n3 = TreeNode(3)        
n4 = TreeNode(4)        
n5 = TreeNode(5)        
n6 = TreeNode(6)        
n7 = TreeNode(7)        

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

s = Solution()
o = s.levelOrder(n1)
print(o)
