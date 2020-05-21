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

    # Approach: sliding array
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(2)]  # sliding array by rows
        
        # intialize
        dp[0][0] = 1
        for j in range(1, n):   # first row
            dp[0][j] = dp[0][j - 1]
        
        now = 1
        for i in range(1, m):
            dp[now][0] = dp[1 - now][0]  # first column of each row
            for j in range(1, n):
                dp[now][j] = dp[1 - now][j] + dp[now][j - 1]
            now = 1 - now
            
        return dp[1 - now][n-1]
