class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    # Approach: 
    def longestIncreasingSubsequence1(self, nums):
        if nums is None or not nums: return 0
            
        dp = [1] * len(nums) # 表示以第i个数字为结尾的最长上升子序列的长度
        
        # 对于每个数字, 枚举前面所有小于自己的数字j, Dp[i] = max{Dp[j]} + 1
        # 如果没有比自己小的, Dp[i] = 1
        for i in range(1, len(nums)):
            for j in range(i):  # 0 to i-1
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        
    
    # Approach: 使用动态规划计算Longest Increasing Subsequence, 并同时打印具体的方案
    def longestIncreasingSubsequence(self, nums):
        if nums is None or not nums: return 0
        
        # state: dp[i] 表示从左到右跳到i的最长sequence的长度
        # initialization: dp[0..n-1] = 1
        dp = [1] * len(nums)
        
        # prev[i]代表dp[i]的最优值是从哪个dp[j]算过来的
        prev = [-1] * len(nums)
        
        # function dp[i]=max{dp[j] + 1},  j<i and nums[j]<nums[i]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        # answer: max(dp[0..n-1])
        longest, last = 0, -1
        for i in range(len(nums)):
            if dp[i] > longest:
                longest = dp[i]
                last = i
        
        path = []
        while last != -1:
            path.append(nums[last])
            last = prev[last]
        print(path[::-1])
        
        return longest

    # Approach: O(nlogn)
    def longestIncreasingSubsequence(self, nums):
        if nums is None or len(nums) == 0: return 0
        
        n = len(nums)
        f = [0] * n         # f[i] 表示以nums[i]结尾的LIS长度
        g = [0] * (n + 1)   # g[i] 表示长度为i的LIS结尾最小是谁
        
        lis = f[0] = 1
        g[1] = nums[0]
        
        for i in range(1, n):
            # 二分查找nums[i]可以放到g数组的哪个数后面; 即查找g数组中第一个不小于nums[i]的位置
            if nums[i] > g[lis]: # 特判, nums[i] 比全部的都大
                f[i] = lis
                lis += 1
                g[lis] = nums[i]
            else:
                l, r =  1, lis 
                while l != r:
                    mid = (l + r) // 2 
                    if g[mid] < nums[i]:
                        l = mid + 1 
                    else:
                        r = mid
                f[i] = l
                g[l] = min(g[l], nums[i])
            
        return lis

Solution().longestIncreasingSubsequence([5, 4, 1, 2, 3])