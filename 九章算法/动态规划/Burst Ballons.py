class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    状态: f[i][j]为扎破 i+1 ~ j-1 号气球, 最多获得的金币数 (i, j为不能扎破的气球, 扎完i~j之间的气球得分f[i][j])
    转移方程: f[i][j] = max i < k < j {f[i][k] + f[k][j] + a[i] * a[k] * a[j]}   (a[k]: 最后扎破的气球)
    """

    # 记忆化搜索
    # memo[i][j] 表示 burst i+1~j-1 这些气球, 留下i, j后的最大收益。
    def maxCoins1(self, nums):
        if not nums:
            return 0

        # [4,1,5] => [1,4,1,5,1]
        nums = [1, *nums, 1] # nums 数组需要前后都添加一个1
            
        return self.memo_search(nums, 0, len(nums) - 1, {})
        
    def memo_search(self, nums, i, j, memo):
        if i == j:
            return 0 
            
        if (i, j) in memo:
            return memo[(i, j)]
        
        best = 0
        for k in range(i + 1, j):
            left = self.memo_search(nums, i, k, memo)
            right = self.memo_search(nums, k, j, memo)
            best = max(best, left + right + nums[i] * nums[k] * nums[j])
        
        memo[(i, j)] = best
        return best
        
    # 区间动态规划
    # dp[i][j] 代表 burst i+1 ~ j-1 这段时间的所有气球之后，只剩下 i,j 的最大收益。
    # 将原来的数组前面和后面增加两个1，最后结果就是 dp[0][n - 1]（burst 掉所有气球只剩两个1）
    def maxCoins2(self, nums):
        if not nums:
            return 0
            
        nums = [1, *nums, 1]
        n = len(nums)
        
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] +  dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][n - 1]
    
    # 另一种写法，dp[i][j] 表示 burst 掉 i~j 这一段气球的最大收益
    def maxCoins(self, nums):
        if not nums:
            return 0
            
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                for k in range(i, j + 1):
                    left = nums[i - 1] if i > 0 else 1
                    right = nums[j + 1] if j < n - 1 else 1
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + left * nums[k] * right)
    
        return dp[0][n - 1]



    def maxCoins_my_ans(self, nums):
        def maxCoins(self, nums):
        if not nums:
            return 0

        # [4,1,5] => [1,4,1,5,1]
        nums = [1, *nums, 1] # nums 数组需要前后都添加一个1

        dp = [[0] * len(nums) for _ in range(len(nums))]
        
        # 初始条件和边界情况:
        # f[0][1] = f[1][2] = ... = f[N][N+1] = 0  相邻气球间无法扎破 f=0
        # for i in range(len(nums) - 1):
        #     j = i + 1
        #     dp[i][j] = 0
        
        for interval in range(2, len(nums)):  # interval=1是初始条件
            # print("interval = ", interval)
            for i in range(0, len(nums) - interval):
                j = i + interval
                # print(i, j)
                dp[i][j] = max([dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j] for k in range(i+1, j)])  #  i < k < j
        
        return dp[0][len(nums) - 1]
        

Solution().maxCoins_my_ans([4, 1, 5])