"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        self.num_islands = 0
        self.father = {}
        
        islands = set([])
        ans = []
        
        for i in operators:
            # already an island
            if (i.x, i.y) in islands:
                ans.append(self.num_islands)
                continue
            
            islands.add((i.x, i.y))
            self.father[(i.x, i.y)] = (i.x, i.y)
            self.num_islands += 1
            
            for d_x, d_y in DIRECTIONS:
                if (i.x + d_x, i.y + d_y) in islands:
                    self.union((i.x + d_x, i.y + d_y), (i.x, i.y))
                
            ans.append(self.num_islands)

        return ans
        
    def union(self, point_a, point_b):
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.num_islands -= 1
        
    def find(self, point):
        path = []
        while point != self.father[point]:
            path.append(point)
            point = self.father[point]
    
        for p in path: # path compression
            self.father[p] = point

        return point