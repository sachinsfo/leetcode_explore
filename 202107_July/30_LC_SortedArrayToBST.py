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

    def sortedArrayToBST(self, nums):
        if not nums:
            return
        
        def construct(arr):
            if not arr:
                return
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            node.left = construct(arr[:mid])
            node.right = construct(arr[mid+1:])
            return node

        return construct(nums)

            
