class Solution:
    """
    @param ListA: The relation between ListB's books
    @param ListB: The relation between ListA's books
    @return: The answer
    """
    def maximumAssociationSet(self, ListA, ListB):
        all_nodes = set(ListA + ListB)
        
        print(all_nodes)
        self.f = {}
        self.size = {}
        for i in all_nodes:
            self.f[i] = i
            self.size[i] = [i]
            
        for i in range(len(ListA)):
            self.union(ListA[i], ListB[i])
        
        # return the value with longest list length
        return self.size[max(self.size, key=lambda x:len(self.size[x]))]
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.f[root_b] = root_a
            # extra step for particular question
            self.size[root_a] += self.size[root_b]
            del self.size[root_b]
    
    def find(self, node):
        path = []
        while node != self.f[node]: # find root node
            path.append(node)
            node = self.f[node]
        for i in path: # path compression
            self.f[i] = node
        return node