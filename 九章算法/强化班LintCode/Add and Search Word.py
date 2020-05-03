'''
addWord("bad") 
addWord("dad") 
addWord("mad") 
search("pad") false 
search("bad") true 
search(".ad") true

("." -> 所有子节点都要尝试 = Recursion)
'''

# 实现前缀树 +
# 在查询的时候将'.'处理为回溯, 遇到'.' 则需要访问每一个子节点判断是否有匹配
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False 
        self.word = None

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word =True
        node.word = word

    # A word could contain the dot character '.' to represent any one letter
    def search(self, word):
        if word is None or self.root is None:
            return False
        return self.dfs(word, self.root)
                
    def dfs(self, word, root):
        # if root is None:
        #     return False
            
        if word == "":
            return root.is_word
        
        if word[0] == ".":
            return any(self.dfs(word[1:], root.children[n]) for n in root.children)
        
        if word[0] in root.children:
            return self.dfs(word[1:], root.children[word[0]])
            
        return False

s = WordDictionary()
s.addWord("abccc")
print(s.search("abcc."))