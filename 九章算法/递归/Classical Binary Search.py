class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        if not nums: 
            return -1
        
        start, end = 0, len(nums) - 1
        if start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                return self.findPosition(nums[:mid+1], target)
            elif nums[mid] < target:
                return mid + self.findPosition(nums[mid:], target)
            else:
                return mid

print(Solution().findPosition([1, 2, 3, 4, 5, 6], 3))


# 不太对