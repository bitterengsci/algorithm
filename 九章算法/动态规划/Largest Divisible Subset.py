# 给一个由无重复的正整数组成的集合，找出满足任意两个元素 (Si, Sj) 都有 Si%Sj = 0 或 Sj%Si = 0 成立的最大子集
'''
dp
首先排序
f[i]代表以nums[i]为最大元素的序列最多有多少个
然后只要nums[k]%nums[i]=0, 则可尝试往f[k]转移
'''
class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset 
    def largestDivisibleSubset(self, nums):
        nums = sorted(nums)

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            dp[i] = max([dp[j] + 1 for j in reversed(range(i)) if nums[i] % nums[j] == 0])

        print(dp)
        return max(dp)

class JiuzhangSolution:
    def largestDivisibleSubset(self, nums):
        dp = [1] * len(nums)
        father = [-1] * len(nums)

        nums.sort()
        m, index = 0, -1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + dp[j] > dp[i]:
                        dp[i] = dp[j] + 1
                        father[i] = j

            if dp[i] >= m:
                m = dp[i]
                index = i

        result = []
        for i in range(m):
            result.append(nums[index])
            index = father[index]

        print(result)
        return result

    '''
    这是nsqrt(a[n])的做法
    用一个dp来表示第i个数有几个因子在nums中，用map来维护这个dp
    dp的转移方程即dp[num] = max(dp[factor] + 1,dp[num])
    用一个pre来记录一个元素上一个最多因子数
    遍历nums,对nums[i]求因子，返回因子序列，并且查找有多少因子在nums中
    查找dp的最大值，并且通过pre获得完整序列
    '''
    def largestDivisibleSubset2(self, nums):
        dp = {}
        pre = {}
        nums = sorted(nums)
        for num in nums:
            dp[num] = 1 
            pre[num] = 0 
        # dp 
        for num in nums:
            for factor in self.get_factor_list(num):
                if factor not in dp:
                    continue 
                if dp[factor] + 1 > dp[num]:
                    dp[num] = dp[factor] + 1 
                    pre[num] = factor
        # get path 
        ans = self.get_path(dp, pre)
        print(ans)
        return ans
    
    # return list of factor of x, except x 
    def get_factor_list(self, x):
        if x == 1:
            return []
        ans = [1]
        i = 2 
        while i * i <= x:
            if x % i != 0:
                i += 1 
                continue
            ans.append(i)
            if x // i != i:
                ans.append(x // i)
            i += 1 
        return ans
    
    def get_path(self, dp, pre):
        max_num = 0 
        max_size = 0 
        for num, size in dp.items():
            if size > max_size:
                max_size = size 
                max_num = num 
        
        path = []    
        path.append(max_num)
        while pre[max_num] in pre:
            max_num = pre[max_num]  
            path.append(max_num)
        return path[::-1]


Solution().largestDivisibleSubset([1, 2, 3, 6, 8, 10])
JiuzhangSolution().largestDivisibleSubset([1, 2, 3, 6, 8, 10])
JiuzhangSolution().largestDivisibleSubset2([1, 2, 3, 6, 8, 10])

Solution().largestDivisibleSubset([1, 2, 3, 6, 8, 10, 20, 100, 200, 400])
JiuzhangSolution().largestDivisibleSubset([1, 2, 3, 6, 8, 10, 20, 100, 200, 400])
JiuzhangSolution().largestDivisibleSubset2([1, 2, 3, 6, 8, 10, 20, 100, 200, 400])