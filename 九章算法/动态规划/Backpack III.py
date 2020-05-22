'''
类似于最基本的01背包, 设 f[i][j] 表示前i种物品装到容量为j的背包里, 能获取的最大价值为多少.

比较简单的转移是直接枚举第i种物品取用多少个 f[i][j] = max{f[i - 1][j - x * A[i]] + x * V[i]}

但是这样速度较慢, 可以优化成 f[i][j] 直接由 f[i][j - A[i]] 转移, 并且从小到大枚举j, 
这样做的含义就是在已经拿过第 i 个物品的之后还可以再拿它. 
也就是说 计算 f[i][j] 时, 初始设置为 f[i - 1][j], 然后 f[i][j] = max(f[i][j], f[i][j - A[i]] + V[i])

另外, 可以使用滚动数组优化, 使用滚动数组之后也不必要手动设置 f[i][j] = f[i - 1][j], 
与01背包使用的滚动数组相反, 这里恰好需要正着枚举容量j, 因而有 f[j] = max(f[j], f[j - A[i]] + V[i])
'''

class Solution:
    def backPackIII(self, A, V, m):
        dp = [0 for i in range(m+1)]
        for (a, v) in zip(A, V):
            for j in range(a, m+1):
                if dp[j - a] + v > dp[j]:
                    dp[j] = dp[j - a] + v
    
        return dp[m]

print(Solution().backPackIII([2, 3, 5, 7], [1, 5, 2, 4], 10), "ans=15")