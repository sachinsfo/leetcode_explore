class Node:
    def __init__(self) -> None:
        self.child = dict()
        self.is_leaf = False 
    
class Trie:
    """
    https://leetcode.com/problems/implement-trie-prefix-tree/discuss/1188645/Python-Solution-Using-Dict
    """
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
        """
        Searches from root to leaf
        """
        node = self.root
        for letter in word:
            if letter in node.child:
                node = node.child[letter]
            else:
                return False
        return node.is_leaf 
        
    
    def startsWith(self, prefix: str):
        """
        Same as search, but, searches only from leaf to a node 
        which is not a leaf
        """
        node = self.root
        for letter in prefix:
            if letter not in node.child:
                return False
            else:
                node = node.child[letter]
        return True
            
    
trie = Trie()
trie.insert('sachin')
v = trie.search('sachin')
print(v)
w = trie.startsWith('sac')
print(w)
