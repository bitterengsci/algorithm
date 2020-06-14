class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    
    # Time Limit Exceeded
    def maxSubArray1(self, nums):
        if len(nums) == 1:
            return nums[0]
        prefix_sum = [0]
        
        maximum = nums[0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)
            maximum = max(maximum, prefix_sum[-1] - min(prefix_sum[:-1]))

        return maximum
        
        
    def maxSubArray(self, nums): # TC=O(N)只需要遍历一遍数组就能找到答案 SC=O(1)
        # max_Sum记录全局最大值，min_Sum记录前i个数中0-k的最小值
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0 # prefix_sum记录前i个数的和
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)
            
        return max_sum