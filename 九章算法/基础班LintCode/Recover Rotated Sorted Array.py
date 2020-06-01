class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    # Approach: find the index of minimum number, recover by 3 step reverse
    def recoverRotatedSortedArray(self, nums):
        if nums[0] < nums[-1]:  # case 1: sorted array
            # idx_min = 0
            return
        
        # case 2: rotated sorted array
        # Find Minimum in Rotated Sorted Array
        # idx_min = self.find_minimum_index(nums)  # not working, as the array may contains duplicate numbers
        
        idx_min = self.find_minimum_index_brute(nums)
        print('offset = ', idx_min)
        
        # 3 step reverse, idx_min can be regarded as the 'offset'
        
        # reverse nums[:idx_min]
        for i in range(idx_min//2):
            nums[i], nums[idx_min -1 - i] = nums[idx_min -1 - i], nums[i]
        # print(nums)
        
        # reverse nums[idx_min:]
        for i in range((len(nums) - idx_min) // 2):
            nums[idx_min + i], nums[-1 - i] = nums[-1 - i], nums[idx_min + i]
        # print(nums)
        
        # reverse all
        for i in range(len(nums)//2):
            nums[i], nums[-1-i] = nums[-1-i], nums[i]
            
    # Find Minimum in Rotated Sorted Array
    def find_minimum_index(self, nums):
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            # x is the First Position <= last number
            if nums[mid] <= nums[-1]:
                end = mid
            else:
                start = mid
        idx_min = start if nums[start] < nums[end] else end
        return idx_min
        
    def find_minimum_index_brute(self, nums):
        min_idx, min_num = 0, nums[0]
        for idx, val in enumerate(nums):
            if val < min_num:
                min_idx, min_num = idx, val
                
        return min_idx