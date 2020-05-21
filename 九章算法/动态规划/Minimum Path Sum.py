class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        R, C = len(grid), len(grid[0])
        dp = [[0] * C for _ in range(R)]  # f[x][y]从起点走到x,y的最短路径
        
        dp[0][0] = grid[0][0]
        
        # intialize: f[i][0] = sum(0,0 ~ i,0), f[0][i] = sum(0,0 ~ 0,i)
        for j in range(1, C):   # first row
            dp[0][j] = grid[0][j] + dp[0][j - 1]
        for i in range(1, R):   # first column
            dp[i][0] = grid[i][0] + dp[i - 1][0]
        
        for i in range(1, R):
            for j in range(1, C):
                dp[i][j] =  grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

        return dp[R-1][C-1]


    # Sliding Array by row, initialization
    def minPathSum_1(self, grid):
        R, C = len(grid), len(grid[0])
        dp = [[0] * C for _ in range(2)]  # 滚动数组 Sliding Array
        
        # intialize, first row
        dp[0][0] = grid[0][0]
        for j in range(1, C):
            dp[0][j] = grid[0][j] + dp[0][j - 1]
            
        now = 1
        for i in range(1, R):
            dp[now][0] = grid[i][0] + dp[1 - now][0]
            for j in range(1, C):
                dp[now][j] = min(dp[1 - now][j], dp[now][j - 1]) + grid[i][j]
            now = 1 - now  # 0 --> 1, 1 --> 0

        return dp[1 - now][C-1]
        
        
    # Sliding Array by row, no intialization, state trasition by conditions
    def minPathSum_2(self, grid):
        R, C = len(grid), len(grid[0])
        dp = [[0] * C for _ in range(2)]  # 滚动数组 Sliding Array
        
        now = 0
        for i in range(R):
            for j in range(C):
                if i == 0 and j == 0:
                    dp[now][j] = grid[0][0]
                    continue
                dp[now][j] = float('inf')
                if i > 0:
                    dp[now][j] = min(dp[now][j], dp[1 - now][j])
                if j > 0:
                    dp[now][j] = min(dp[now][j], dp[now][j - 1])
                dp[now][j] +=  grid[i][j]
            now = 1 - now  # 0 --> 1, 1 --> 0

        return dp[1 - now][C-1]