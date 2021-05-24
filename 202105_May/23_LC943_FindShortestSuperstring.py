# @Author  : github.com/sachinsfo

from typing import List
import math
from heapq import heappush as hpush, merge
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
    def shortestSuperString(self, words):
        """
        Greedy approach - may have issues in few cases 
        Did not pass the leetcode grader!
        """
        
        def shortest(s1, s2):
            m = len(s1)
            n = len(s2)
            overlap_len1 = 0
            for i in range(1, m+1):
                if i <= n:
                    _s1 = s1[:i]
                    _s2 = s2[-i:]
                    if _s1 == _s2:
                        overlap_len1 = i 
                else:
                    break
            
            overlap_len2 = 0
            for i in range(1, m+1):
                if i <= n:
                    _s1 = s1[-i:]
                    _s2 = s2[:i]
                    if _s1 == _s2:
                        overlap_len2 = i 
                else:
                    break
                
            if overlap_len1 == overlap_len2 == 0:
                return s2 + s1
            
            if overlap_len1 >= overlap_len2:
                return s2 + s1[overlap_len1:]
            return s1 + s2[overlap_len2:]
        
        while True:
            N = len(words)
            if N == 1:
                break

            ix1 = ix2 = 0
            new_str = ''
            max_length = -1
            for i in range(N-1):
                for j in range(i+1, N):
                    first = words[i]
                    second = words[j]
                    result = shortest(first, second)
                    # print(first, second, resultear
                    
                    a = len(first)
                    b = len(second)
                    c = len(result)
                    
                    saved_len = a + b - c
                    if saved_len > max_length:
                        max_length = saved_len
                        ix1 = i
                        ix2 = j
                        new_str = result
            w1 = words[ix1]
            w2 = words[ix2]
            words.remove(w1)
            words.remove(w2)
            words.append(new_str)
        return words.pop()
        
index = 0
for _input, expected_output in \
        [
            (["alex","loves","leetcode"], 'alexlovesleetcode'),
            (["catg","ctaagt","gcta","ttca","atgcatc"], 'gctaagttcatgcatc'),
            # (,),
        ]:
    s = Solution()
    index += 1
    actual_output = s.shortestSuperString(_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')