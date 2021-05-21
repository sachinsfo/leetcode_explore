class Node:
    def __init__(self) -> None:
        self.child = dict()
        self.is_leaf = False

class Trie:
    def __init__(self) -> None:
        self.root = Node()
    
    def insert(self, word: str):
        node = self.root
        for letter in word:
            if letter not in node.child:
                node.child[letter] = Node()
            node = node.child[letter]
        node.is_leaf = True
    
    def search(self, word: str):
        node = self.root
        for letter in word:
            if letter not in node.child:
                return False
            node = node.child[letter]
        return node.is_leaf
    
    def startsWith(self, prefix: str):
        node = self.root
        for letter in prefix:
            if letter not in node.child:
                return False
            node = node.child[letter]
        return True 

trie = Trie()
trie.insert('leetcode')
trie.insert('leetcoder')
trie.insert('leeter')
a = trie.search('leetcode')
b = trie.search('leeeet')
c = trie.searchPrefix('leet')
d = trie.searchPrefix('leeet')

assert a == True, "{} not found!".format(a)
assert b == False, "{} not found!".format(b)
assert c == True, "{} not found!".format(c)
assert d == False, "{} not found!".format(d)

print('All passed!')
