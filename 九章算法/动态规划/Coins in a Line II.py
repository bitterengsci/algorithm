class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        # f[i]为一方在面对a[i..n-1]这些数字时, 能得到的最大的与对手的数字差 
        # 转移方程 f[i] = max{a[i] - f[i+1], a[i] + a[i + 1] - f[i + 2]}
        
        if len(values) <= 2:
            return True
        
        dp = [0] * (len(values) + 1 )
        
        dp[-1] = 0              # facing [ ]
        dp[-2] = values[-1]     # facing [n-1]
        
        for i in reversed(range(len(values) - 1)):
            dp[i] = max(values[i] - dp[i+1], values[i] + values[i+1] - dp[i+2])
        
        return dp[0] >= 0