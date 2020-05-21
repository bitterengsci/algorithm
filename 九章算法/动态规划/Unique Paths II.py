class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * C for _ in range(R)]  # f[x][y]从起点走到x,y的path数
        
        if obstacleGrid[0][0]:
            return 0
        dp[0][0] = 1
        
        # intialize
        for j in range(1, C):   # first row
            dp[0][j] = dp[0][j - 1] if not obstacleGrid[0][j] else 0
        for i in range(1, R):   # first column
            dp[i][0] = dp[i - 1][0] if not obstacleGrid[i][0] else 0
        
        for i in range(1, R):
            for j in range(1, C):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if not obstacleGrid[i][j] else 0

        return dp[R-1][C-1]