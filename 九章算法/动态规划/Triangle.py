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
    def minimumTotal3(self, triangle):
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
         
    

    # Approach 4: Dynamic Programming (Iterative Bottom Up)
    def minimumTotal4(self, triangle):
        f = {}  # define the state 定义状态数组 f: 从(i, j)开始走到底的最小路径长度
        for i in range(len(triangle)): # initialization 初始化, 先有值
            f[(len(triangle) - 1, i)] = triangle[len(triangle) - 1][i]
        
        # iteration for solution 循环递推求解
        for i in reversed(range(len(triangle)-1)):
            for j in range(0, i+1):
                f[(i, j)] = triangle[i][j] + min(f[(i + 1, j)], f[(i + 1, j + 1)])
        return f[(0, 0)]  # result 求结果=起点
    


    # Approach 5: Dynamic Programming (Iterative Top Down)
    def minimumTotal(self, triangle):
        f = {(0, 0): triangle[0][0]}  # 初始化, 起点 f: 从(0,0)开始走到(i,j)最小路径长度
        
        # 初始化三角形的左边和右边 (左边无左上角, 右边无右上角)
        for i in range(1, len(triangle)):
            f[(i, 0)] = f[(i - 1, 0)] + triangle[i][0]
            f[(i, i)] = f[(i - 1, i - 1)] + triangle[i][i]
            
        # top Down (亦可不初始化三角形左右边, 在此加入if语句)
        for i in range(1, len(triangle)):
            for j in range(1, i):
                f[(i, j)] = triangle[i][j] + min(f[(i - 1, j)], f[(i - 1, j - 1)])
                
        return min([f[(len(triangle) - 1, j)] for j in range(len(triangle))]) # 底层最小值
        
    # SC优化: 滚动数组  [i % 2], 这样只用两个一维数组储存f即可