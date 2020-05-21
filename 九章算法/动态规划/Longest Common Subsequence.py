class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
    
        dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
        
        # initialization
        for j in range(len(B)+1):
            dp[0][j] = 0
        for i in range(len(A)+1):
            dp[i][0] = 0
            
        # state transitition
        # f[i][j] = max{f[i-1][j], f[i][j-1], f[i-1][j-1]+1 | A[i-1]=B[j-1]}
        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1] :
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
                else: 
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[-1][-1]