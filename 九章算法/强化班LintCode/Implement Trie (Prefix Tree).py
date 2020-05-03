class TrieNode:
    def __init__(self):
        self.children = {}
        # for i in range(25): # 26=字母表大小
        #     self.children = None
        self.is_word = False
        self.word = "" # optional
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root # 都从根节点出发
        for c in word:
            if c not in node.children: # [ord(c)-ord('a')]
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True
        node.word = word
        
    # return the node in the trie if exists, else None
    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node

    # if the word is in the trie
    def search(self, word: str):
        node = self.find(word)
        return node is not None and node.is_word

    # if there is any word in the trie that starts with the given prefix
    def startsWith(self, prefix):
        return self.find(prefix) is not None