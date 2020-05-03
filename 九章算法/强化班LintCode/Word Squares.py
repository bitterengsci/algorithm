class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word_list = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word_list.append(word)
        node.is_word = True

    def find(self, word):
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
        return node
        
    def get_words_with_prefix(self, prefix):
        node = self.find(prefix)
        return [] if node is None else node.word_list
        
    def contains(self, word):
        node = self.find(word)
        return node is not None and node.is_word


# 使用排列式搜索 + Trie
class Solution:
    # Given a set of words without duplicates, return all word squares
    def wordSquares(self, words):
        
        trie = Trie()
        for w in words:
            trie.add(w)
            
        squares = []
        for w in words:
            self.dfs(trie, [w], squares) # search with dfs
        return squares
        
    def dfs(self, trie, square, squares):
        n = len(square[0])
        idx = len(square)
        if idx == n:
            squares.append(list(square))
            return
        
        # Pruning, it's ok to remove it, but will be slower
        for row_index in range(idx, n):
            prefix = ''.join([square[i][row_index] for i in range(idx)])
            if trie.find(prefix) is None:
                return
        
        prefix = ''.join([square[i][idx] for i in range(idx)])
        for word in trie.get_words_with_prefix(prefix):
            self.dfs(trie, square + [word], squares)