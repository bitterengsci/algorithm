'''
输入: n=5, edge=[[0, 1], [0, 2], [0, 3], [1, 4]] 输出:true
输入: n=5, edge= [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]] 输出:false
'''

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if n - 1 != len(edges):
            return False
        self.father = {}
        self.num_islands = n
        
        for i in range(n):
            self.father[i] = i
        
        for i in edges:
            self.union(i[0], i[1])
        
        return self.num_islands == 1
        
    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]
        
        for p in path:
            self.father[p] = node
        
        return node
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.num_islands -= 1