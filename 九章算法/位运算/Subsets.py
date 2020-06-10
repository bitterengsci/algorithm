class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    # Non Recursion 非递归版本，利用二进制的方式逐个枚举 subsets
    def subsets(self, nums):
        nums.sort()
        
        results = []
        for i in range(1 << len(nums)):
            subset = []
            for j in range(len(nums)):
                # check whether the jth digit in i's binary representation is 1
                if i & (1 << j):
                    subset.append(nums[j])
                    
            results.append(subset)
            
        return results