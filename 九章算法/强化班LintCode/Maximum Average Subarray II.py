class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        if not nums: return 0
        
        # 上下界怎么确定?
        start, end = min(nums), max(nums)
        
        while end - start > 1e-5:  # 自定义精度
            mid = start + (end - start) / 2  # 精度不为1, 则不是//2 !!
            if self.average_large_than_T(nums, k, mid):
                start = mid
            else:
                end = mid
                
        return start

    # this made TLE
    def average_large_than_T_badbad(self, nums, k, avg):
        B = [i - avg for i in nums]  # B[i] = A[i] - avg
        # cumulative sum for B
        prefix_sum = [0]   # len = len(B) + 1
        for i in range(len(B)):   
            prefix_sum.append(prefix_sum[-1] + B[i])
        
        for i in range(1, len(prefix_sum)):
            for j in range(i, len(prefix_sum)):
                if prefix_sum[j] - prefix_sum[i-1] >= 0 and j - i + 1 >= k:
                    return True
        return False
    
        
    def average_large_than_T(self, nums, k, average):
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num - average)
            
        min_prefix_sum = 0
        for i in range(k, len(nums) + 1):
            if prefix_sum[i] - min_prefix_sum >= 0:
                return True
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i - k + 1])
            
        return False
                