class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]  # f[x][y]从起点走到x,y的path数
        
        dp[0][0] = 1
        
        # intialize
        for j in range(1, n):   # first row
            dp[0][j] = dp[0][j - 1]
        for i in range(1, m):   # first column
            dp[i][0] = dp[i - 1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]