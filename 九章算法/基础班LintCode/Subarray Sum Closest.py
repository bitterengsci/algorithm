class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    
    # 前缀和优化 + 排序贪心
    def subarraySumClosest(self, nums):
        prefix_sum = [(0, -1)]   # sum, index
        for i, num in enumerate(nums):
            prefix_sum.append((prefix_sum[-1][0] + num, i))
        prefix_sum.sort()
        
        closest, answer = sys.maxsize, []
        for i in range(1, len(prefix_sum)):
            if closest > prefix_sum[i][0] - prefix_sum[i - 1][0]:
                closest = prefix_sum[i][0] - prefix_sum[i - 1][0]
                left = min(prefix_sum[i - 1][1], prefix_sum[i][1]) + 1
                right = max(prefix_sum[i - 1][1], prefix_sum[i][1])
                answer = [left, right]
        
        return answer