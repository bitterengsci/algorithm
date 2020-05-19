class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    
    # Approach 1: DFS-traverse  (TLE)
    def minimumTotal1(self, triangle):
        best = self.traverse(0, 0, 0, triangle, float('inf'))
        return best # best is the answer
       
    def traverse(self, x, y, pathsum, triangle, best):
        if x == len(triangle): # found a whole path from top to bottom
            if pathsum < best:
                return pathsum
        
        return min(self.traverse(x + 1, y, pathsum + triangle[x][y], triangle, best), self.traverse(x + 1, y + 1, pathsum + triangle[x][y], triangle, best))
        


    # Approach 2: DFS-Divide Conquer (TLE)
    def minimumTotal2(self, triangle):
        return self.dc(0, 0, triangle) # 从(0, 0)出发走到最底层
        
    def dc(self, x, y, triangle):
        if x == len(triangle):    # None节点, 0..n-1层才有值
            return 0    # if x == len(triangle) - 1: return triangle[x][y] #也可
         
        return triangle[x][y] + min(self.dc(x + 1, y, triangle), self.dc(x + 1, y + 1, triangle)) # 左右两个节点中的最小值



    # Approach 3: DFS-Divide Conquer + Memorization
    def minimumTotal(self, triangle):
        
        return self.dc_memo(0, 0, triangle, {})
    
    def dc_memo(self, x, y, triangle, memo): # return minimum path from (x, y) to bottom
        if x == len(triangle): # row index from 0 to n-1 
            return 0
            
        # if already got the minimum path from (x, y) to bottom; just return
        if (x, y) in memo:
            return memo[(x, y)]
            
        # set before return
        memo[(x, y)] = triangle[x][y] + min(self.dc_memo(x + 1, y, triangle, memo), self.dc_memo(x + 1, y + 1, triangle, memo))
        return memo[(x, y)]


