# Approach: 前缀和数组 cumulative sum from the beginning(Memoization) TC=O(N^2), SC=O(N)

# Approach: Two Pointers 同向双指针 O(n) solution
# Initialize left pointer to 0 and sum to 0
# Iterate over the nums:
#   - Add nums[i] to sum
#   - While sum is greater than or equal to s:
#       * Update ans=min(ans,i+1−left), where i+1−left is the size of current subarray
#       * It means that the first index can safely be incremented, since, the minimum subarray starting with this index with sum≥s has been achieved
#       * Subtract nums[left] from sum and increment left
def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    minlen = len(nums) + 1
    
    j, sums = 0, 0 
    # sums = sum from i(inclusive) to j(inclusive)
    
    for i in range(len(nums)):  # for loop 左指针
        while j < len(nums):    # while loop 右指针
            sums += nums[j]
            if sums >= s:
                minlen = min(minlen, j - i + 1)
                sums -= nums[j]
                break
            j += 1

        sums -= nums[i]
    
    if minlen == len(nums) + 1:
        return 0
    return minlen

# 九章算法答案
def minSubArrayLen(self, s, nums):
    if nums is None or len(nums) == 0:
        return 0

    minLength = len(nums) + 1
    sum = 0
    j = 0
    for i in range(len(nums)):
        while j < len(nums) and sum < s:
            sum += nums[j]
            j += 1
        if sum >= s:
            minLength = min(minLength, j - i)

        sum -= nums[i]

    if minLength == len(nums) + 1:
        return 0
    return minLength
# Approach: TC=O(n logn), How???