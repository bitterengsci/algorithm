class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        if n == 0: 
            return False
        if n == 1 or n == 2:
            return True
        dp = [None] * (n + 1)
        
        dp[0] = False           # first player loses
        dp[1] = dp[2] = True    # first play wins
        
        for i in range(3, n + 1): # 3 coins to n coins
        
            # dp[i] False only when both dp[i-1] dp[i-2] are True
            dp[i] = dp[i-1] == False or dp[i-2] == False
        
        return dp[n]
            