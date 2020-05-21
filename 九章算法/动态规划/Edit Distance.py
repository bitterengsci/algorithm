class Solution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.
    """
    def minDistance(self, word1, word2):
        
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        # initialization
        for j in range(len(word2) + 1):
            dp[0][j] = j
        for i in range(len(word1) + 1):
            dp[i][0] = i
            
        # state transition
        # f[i][j] = min{f[i][j-1]+1, f[i-1][j-1]+1, f[i-1][j]+1, f[i-1][j-1]|A[i-1]=B[j-1]}
        
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j-1] + 1, dp[i-1][j] + 1)
        
        return dp[-1][-1]