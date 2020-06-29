class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    # DFS
    def subsets(self, nums):
        
        results = []
        self.dfs(sorted(nums), 0, [], results)
        
        return results
        
        
    def dfs(self, nums, idx, curr, results):
        if idx == len(nums):
            results.append(curr)  
            return
        
        self.dfs(nums, idx + 1, curr + [nums[idx]], results)
        self.dfs(nums, idx + 1, curr, results)
        
    # Bit Manipulation