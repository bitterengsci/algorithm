class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # if n == 0: return 0
        dp = [0, 1, 2]  # base cases
        
        for i in range(3, n + 1):
            dp.append(dp[i-1] + dp[i-2])
            
        return dp[n]