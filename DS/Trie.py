class Node:
    def __init__(self, val, isWord=False):
        self.val = val
        self.child = {}
        self.isWord = isWord

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node("")
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root 
        for ch in word:
            if ch not in current.child:
                current.child[ch] = Node(ch)
            current = current.child.get(ch)
        current.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root 
        for ch in word:
            if ch in current.child:
                current = current.child.get(ch)
            else:
                return False
        return current.isWord
                

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root 
        for ch in prefix:
            if ch in current.child:
                current = current.child.get(ch)
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
word="Hello"
prefix="He"
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(param_2)
print(param_3)

