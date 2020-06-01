class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # sorted array
        if nums[-1] > nums[0]:
            return nums[0]
        
        # rotated sorted array
        # x is the First Position <= last number
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] <= nums[-1]:
                end = mid
            else:
                start = mid
        
        return min(nums[start], nums[end])