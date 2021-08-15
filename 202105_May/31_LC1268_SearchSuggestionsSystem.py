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
        self.data = dict()
    
    def initialize(self, products):
        for i in range(1, len(products)):
            key = products[:i]
            self.data[key] = self.data.setdefault(key, []) + [products[i-1]]

    def suggestedProducts(self, products, searchWord):
        self.initialize(products)
        
index = 0
for _input, expected_output in \
        [
            ((["mobile","mouse","moneypot","monitor","mousepad"], 'mouse'),[
                ["mobile","moneypot","monitor"],
                ["mobile","moneypot","monitor"],
                ["mouse","mousepad"],
                ["mouse","mousepad"],
                ["mouse","mousepad"]
                ]),
            ((['havana'], 'havana'),[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]),
            ((["bags","baggage","banner","box","cloths"],'bags'),[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]),
            ((["havana"],'tatiana'),[[],[],[],[],[],[],[]]),
        ]:
    s = Solution()
    index += 1
    actual_output = s.suggestedProducts(*_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
