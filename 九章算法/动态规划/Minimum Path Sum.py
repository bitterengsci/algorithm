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