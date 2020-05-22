class Solution:
    """
    @param A: An integer array
    @param K: A positive integer (K <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum1_wrong(self, A, K, target):
        # dp[i][k][s]表示有多少种方法可以在前i个数中选出k个, 使得它们的和是s
        dp = [[[0] * (target + 1) for _ in range(K + 1)] for _ in range(len(A) + 1)]
        
        # initialization
        dp[0][0][0] = 1
        for s in range(target + 1):
            dp[0][0][s] = 0
            
        # state transition f[0][0~K][0~Target]  ...  f[N][0~K][0~Target]
        for i in range(1, len(A) + 1):
            for k in range(K + 1):
                for s in range(target + 1):
                    if k >= 1 and s >= A[i-1]:
                        dp[i][k][s] = dp[i-1][k-1][s-A[i-1]]
                    dp[i][k][s] += dp[i-1][k][s]
        
        # TC=O(N*K*Target) 三维, SC=O(N*K*Target)
        # 将k-s看做一个平面, 计算f[i][k][s]只需要当前面和前一面, 故可以用滚动数组优化至 2 * K * Target
        
        print(dp)
        # 答案是f[N][K][Target]
        return dp[-1][-1][-1]
        

        
    def kSum(self, A, k, target):
        dp = [ [[0] * (target + 1) for _ in range(k + 1)],
               [[0] * (target + 1) for _ in range(k + 1)],
             ]
        
        # dp[i][j][s] 前 i 个数里挑出 j 个数，和为 s
        dp[0][0][0] = 1
        for i in range(1, len(A) + 1):
            dp[i % 2][0][0] = 1
            for j in range(1, min(k + 1, i + 1)):
                for s in range(1, target + 1):
                    dp[i % 2][j][s] = dp[(i - 1) % 2][j][s]
                    if s >= A[i - 1]:
                        dp[i % 2][j][s] += dp[(i - 1) % 2][j - 1][s - A[i - 1]]
                        
        return dp[len(A) % 2][k][target]