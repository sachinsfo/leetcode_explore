'''
Tile Arranger
Programming challenge description:
Write an algorithm to determine whether a collection of tiles can be rearranged to form a given word. Each tile has 1..N letters. You do not have to use each tile, but you cannot use any tile more than once. There can be several identical tiles.

You may assume len(word) >= 1 and size(tiles) >= 1

Input:
Newline separated list of strings provided through STDIN

<tile 0>

<tile 1>

..

Output:
"true" or "false"
'''

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

    def rearrange(self, target, rem_tiles, word_formed=''):
        if target == '':
            return 'true'
    
        len_target = len(target)
        for index in range(len(rem_tiles)):
            tile = rem_tiles[index]
            len_tile = len(tile)
            if len_tile <= len_target:
                prefix = target[:len_tile]
                if prefix == tile:
                    suffix = target[len_tile:]
                    word_formed += prefix
                    r_tiles = rem_tiles[:index] + rem_tiles[index+1:]
                    value = self.rearrange(suffix, r_tiles, word_formed)
                    if value == 'true':
                        return 'true'
    
        if target == '':
            return 'true'
        return 'false'
        
index = 0
for _input, expected_output in \
        [
            (('catsanddogs', ['cat', 'sand', 'dog', 's']), 'true'),
            (('catsanddogss', ['cat', 'sand', 'dog', 's']), 'false'),
            (('catsanddogs', ['cat', 'sand', 'dog', 'so']), 'false'),
            (('catsanddogs', ['cat', 'sand', 'dog', 's']), 'true'),
            (('catsanddogscat', ['cat', 'cat', 'sand', 'dog', 's']), 'true'),
            (('foobarbaz', ['foo', 'foob', 'ba', 'r', 'z']), 'false'),
            (('foobarbaz', ['foo', 'foob', 'ba', 'ba', 'r', 'z']), 'true'),
            (('foobarbaz', ['fo', 'foob', 'ba', 'ba', 'r', 'z']), 'false'),
            (('', ['fo', 'foob', 'ba', 'ba', 'r', 'z']), 'true'),
            (('foobarbaz', ['foobarbaz']), 'true'),
        ]:
    s = Solution()
    index += 1
    actual_output = s.rearrange(*_input)
    assert actual_output == expected_output, "tc{} failed => {}".format(index, actual_output)
else:
    print('\n*** All tests passed successfully! ***')
