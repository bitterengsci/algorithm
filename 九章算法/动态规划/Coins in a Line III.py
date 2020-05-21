# no permission to this problem, sadly

'''
- 状态: 设f[i][j]为一方先手在面对a[i..j]这些数字时, 能得到的最大的与对手的 数字差 --> 区间型动态规划
- 转移方程: 取头, 剩下数字 i+1 ~ j + 取尾, 剩下数字 i ~ j-1
    f[i][j] = max{a[i] - f[i+1][j], a[j] - f[i][j-1]}
- 初始条件: f[i][i] = a[i]  (面对一个数字 -> 拿走!)
- 计算顺序:
    长度1 f[0][0], f[1][1], f[2][2], ..., f[N-1][N-1]  
    长度2 f[0][1], ..., f[N-2][N-1]
    长度N f[0][N-1]
- 如果f[0][N-1]>=0, 先手Alice必赢, 否则必输
- 时间复杂度O(N2), 空间复杂度O(N2), 也可以用记忆化搜索; 也可以滚动数组, 滚动方向为对角线, 从左下到右上 (但定义比较麻烦)
'''

def coins(nums):
    if not nums or len(nums) == 1:
        return True
    
    dp = [[0] * len(nums) for _ in range(len(nums))]

    # initialization, 面对一个数字 -> 拿走
    for i in range(len(nums)):
        dp[i][i] = nums[i]

    # state transition
    for interval in range(1, len(nums)):
        print("interval = ", interval)
        for i in range(0, len(nums) - interval):
            j = i + interval
            dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

    return dp[0][len(nums)-1]>=0



# 不知道对不对。。。 就当对吧。。。
print(coins([1, 5, 233, 7]))