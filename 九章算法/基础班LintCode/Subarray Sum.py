class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):  # TLE
        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)
            
        for i in range(len(prefix_sum) - 1):
            for j in range(i+1, len(prefix_sum)):
                if prefix_sum[j] - prefix_sum[i] == 0:
                    return i, j-1
                
        return -1, -1
    
    # 前缀和 + hash
    def subarraySum1(self, nums):
        prefix_hash = {0: -1}
        
        prefix_sum = 0
        for i in range(len(nums)):   # 用enumerate
            prefix_sum += nums[i]
            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, i
            prefix_hash[prefix_sum] = i
            
        return -1, -1