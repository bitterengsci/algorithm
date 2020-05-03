DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class TrieNode: # define node in a trie
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add(self, word): # insert the word into trie
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()   #在此节点申请节点
            node = node.children[c] # continue traversing
        node.is_word = True
        node.word = word        #存入单词
        
    def find(self, word):	
        node = self.root
        for c in word:
            node = node.children.get(c)
            if node is None:
                return None
                
        return node


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    # Approach: 不用Trie，直接使用hashset的方法
    def wordSearchII(self, board, words):
        if board is None or len(board) == 0:
            return []
        
        # pre-process
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.search(board, i, j, board[i][j], word_set, prefix_set, set([(i, j)]), result)
                
        return list(result)
        
    def search(self, board, x, y, word, word_set, prefix_set, visited, result):
        if word not in prefix_set:
            return
        
        if word in word_set:
            result.add(word)
        
        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_) or (x_, y_) in visited:
                continue
            
            visited.add((x_, y_))
            self.search(board, x_, y_, word + board[x_][y_], word_set, prefix_set, visited, result)
            visited.remove((x_, y_))
    
    # Approach: 使用Trie进行剪枝
    '''
    考点：
    - dfs
    - Trie树, 一种树形结构, 哈希树的变种
            典型应用是用于统计，排序和保存大量的字符串(但不仅限于字符串), 所以经常被搜索引擎系统用于文本词频统计
    题解：
        首先建立字典树，字典树从root开始。利用字母的公共前缀建树。
        遍历字母矩阵，将字母矩阵的每个字母，从root开始dfs搜索，搜索到底部时，将字符串存入答案返回即。
    '''

    def wordSearchII_trie(self, board, words):
        if board is None or len(board) == 0:
            return []
        
        trie = Trie()
        for w in words:
            trie.add(w)
            
        result = set()
        
        # traverse the board/matrix, start dfs with each entry
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.root.children.get(board[i][j]), set([(i, j)]), result)
                
        return list(result)
    
    def dfs(self, board, x, y, node, visited, result): # search..
        if node is None:
            return
        
        if node.is_word:
            result.add(node.word)
            
        for delta_x, delta_y in DIRECTIONS: # search for 4 directions
            x_ = x + delta_x
            y_ = y + delta_y
            
            if not self.inside(board, x_, y_) or (x_, y_) in visited:
                continue
            
            # valid direction, do explore..
            visited.add((x_, y_))
            self.dfs(board, x_, y_, node.children.get(board[x_][y_]), visited,result)
            visited.remove((x_, y_))
        
    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])
        
