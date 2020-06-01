class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # find the first position
        first = self.first_position(A, target)
        # find the last position
        last = self.last_position(A, target)
        
        return [first, last]


    def first_position(self, nums, target):
        if not nums: return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
        
    def last_position(self, nums, target):
        
        if not nums: return -1
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start
        return -1
        