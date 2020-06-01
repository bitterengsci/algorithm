class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # strictly decreasing
        if len(nums) == 1 or nums[0] > nums[1]:
            return nums[0]
        # strictly increasing 
        if nums[-1] > nums[-2]:
            return nums[-1]
        
        # increase then decrease
        start, end = 1, len(nums) - 2
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] < nums[mid+1]:
                start = mid
            else:
                end = mid
                
        if nums[end] > nums[end+1]:
            return nums[end]
        return nums[start]