class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        nums.sort()
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            # smaller than or equal to
            if sum([i <= nums[mid] for i in nums[:mid+1]]) <= nums[mid]:
                start = mid
            else:
                end = mid
                
        if sum([i <= nums[start] for i in nums]) <= start:
            return nums[start]
            
        return nums[end]