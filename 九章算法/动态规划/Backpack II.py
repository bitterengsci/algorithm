class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    
    # There are n items and a backpack with size m. 
    # Given array A representing the size of each item and array V representing the value of each item.
    
    # Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
    # Output: 9
    
    # 状态转移方程 f[i][j] = max(f[i - 1][j], f[i - 1][j - A[i]] + V[i])
    # SC = O(nm), n = len(A)
    
    def backPackII(self, m, A, V): # m:背包容量 A:物品大小 V:物品价值
    
        dp = [[0] * (m + 1) for _ in range(len(A) + 1)]
        
        for i in range(len(A)):         # row = num of objects
            for j in range(1, m + 1):   # col = values
                if j - A[i] < 0:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j - A[i]] + V[i])
        
        [print(line) for line in dp]
        return dp[-1][-1]   # dp[len(A) + 1][m]

    # 滚动数组优化空间至O(m)
    def backPackII1(self, m, A, V): # m:背包容量 A:物品大小 V:物品价值
        f = [0 for i in range(m+1)]
        for i in range(len(A)):
            for j in range(m, A[i]-1, -1):
                f[j] = max(f[j] , f[j-A[i]] + V[i])
        return f[m]
        
    def backPackII2(self, m, A, V): # m:背包容量 A:物品大小 V:物品价值
        dp = [[0] * (m + 1), [0] * (m + 1)]     # 滚动数组
        
        for i in range(1, len(A) + 1):  # i = index of object
            dp[i % 2][0] = 0            
            for j in range(1, m + 1):   # j = total value of objects (0...m)
                dp[i % 2][j] = dp[(i - 1) % 2][j]
                if A[i - 1] <= j:
                    dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - A[i - 1]] + V[i - 1])
        return dp[len(A) % 2][m]
