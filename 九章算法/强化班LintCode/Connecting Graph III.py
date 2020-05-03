'''
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.

Support the following method:
    connect(a, b), an edge to connect node a and node b
    query(), Returns the number of connected component in the graph

Example:
    n = 5 
    query() 输出 5 
    connect(1, 2) 
    query() 输出 4 
    connect(2, 4) 
    query() 输出 3

'''
class ConnectingGraph3:
    def __init__(self, n): # n = number of nodes
        # initialize data structure
        self.f = {}  # fathers
        self.num_islands = n # number of islands
        
        # UF initialization
        for i in range(1, n+1):
            self.f[i] = i
    
    def find(self, x):
        root = x
        while self.f[root] != root:
            root =self.f[root]
            
        while x != root:
            x, self.f[x] = self.f[x], root
        return root

    def connect(self, a, b):  # 必须通过根节点合并
        fx = self.find(a)
        fy = self.find(b)
        if fx != fy:
            self.num_islands -= 1
            self.f[fx] = fy

    def query(self):
        return self.num_islands