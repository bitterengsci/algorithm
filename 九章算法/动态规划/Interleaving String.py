class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """
    def isInterleave(self, s1, s2, s3):
        # 状态: f[i][j] = X前i+j个字符是否由A前i个字符和B前j个字符交错形成
        # 转移方程: f[i][j] = (f[i-1][j] AND X[i+j-1]==A[i-1]) OR (f[i][j-1] AND X[i+j-1]==B[j-1])
        # 初始条件: f[0][0] = True 空串和空串可以组成空串
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        
        # initialization 空串和空串可以组成空串
        dp[0][0] = True
            
        # state transition
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if not (i == 0 and j == 0):
                    dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1]) or (dp[i][j-1] and s3[i+j-1] == s2[j-1])
 
        return dp[-1][-1]