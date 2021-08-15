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

class Graph:
    def __init__(self, vertices):
        self.graph = dict()
        # vertices is a list of tuples
        for vertex in vertices:
            self.addEdge(vertex[0], vertex[1])
    
    def addEdge(self, u, v):
        self.graph[u] = self.graph.setdefault(u, []) + [v]
    
    def getGraph(self):
        return self.graph

    def __len__(self) -> int:
        return len(self.graph)
   
    def __repr__(self) -> str:
        result = ''
        for k, v in self.graph.items():
            for _v in v:
                result += '{}->{}\n'.format(k, _v)
        return result

class Solution:
    def __init__(self):
        pass

    def TwoSum(self, nums, target):
        memo = dict()
        for i in range(len(nums)):
            n = nums[i]
            diff = target - n
            if diff in memo:
                return [memo[diff], i]
            memo[n] = i


        
index = 0
for _input, expected_output in \
        [
            (([2, 7, 11, 15], 9),[0, 1]),
            (([3, 2, 4], 6), [1, 2]),
            (([3, 3], 6), [0, 1]),
        ]:
    s = Solution()
    index += 1
    try:
        actual_output = s.TwoSum(*_input)
        assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
    except Exception as e:
        print('tc{}: Exception occured: {}'.format(index, e))
        break
else:
    print('\n*** All tests passed successfully! ***')
