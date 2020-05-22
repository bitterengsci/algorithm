def backPack(self, m, A):
        dp = [[False] * (m + 1) for _ in range(len(A) + 1)]
        
        # initialization
        dp[0][0] = True  # 0个物品可以拼出重量0
        for j in range(1, m + 1): # 0个物品不能拼出大于0的重量
            dp[0][j] = False
        
        # state transition
        for i in range(1, len(A) + 1):
            for w in range(m + 1):
                if w-A[i-1] >= 0:
                    dp[i][w] = dp[i-1][w-A[i-1]]
                dp[i][w] = dp[i][w] or dp[i-1][w]
        
        # 答案是最大的j使得f[n][j]=True
        for j in reversed(range(m + 1)):
            if dp[-1][j]:
                return j