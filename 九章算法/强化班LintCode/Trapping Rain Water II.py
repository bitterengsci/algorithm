import heapq

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param heights: a matrix of integers
    @return: an integer
    """
    
    def trapRainWater(self, heights):
        
        if not heights:
            return 0
    
        # initialization
        self.R, self.C = len(heights), len(heights[0])
        self.visited = set()
        self.borders = []  # a minheap
        
        for index in range(self.R):
            self.add(index, 0, heights[index][0])
            self.add(index, self.C - 1, heights[index][self.C - 1])
            
        for index in range(self.C):
            self.add(0, index, heights[0][index])
            self.add(self.R - 1, index, heights[self.R - 1][index])
        
        water = 0
        while self.borders:
            height, x, y = heapq.heappop(self.borders)
            for new_x, new_y in self.adjacent(x, y):
                water += max(0, height - heights[new_x][new_y])
                self.add(new_x, new_y, max(height, heights[new_x][new_y]))

        return water
            
    def add(self, x, y, height):
        # add x, y, height to borders
        heapq.heappush(self.borders, (height, x, y))
        self.visited.add((x, y))
        
    def adjacent(self, x, y):
        adj = []
        for delta_x, delta_y in DIRECTIONS:
            new_x, new_y = x + delta_x, y + delta_y
            if 0 <= new_x < self.R and 0 <= new_y < self.C and (new_x, new_y) not in self.visited:
                adj.append((new_x, new_y))
        return adj