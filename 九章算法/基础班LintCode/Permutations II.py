class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """
    def permuteUnique_recursion(self, nums):
        results = []
        
        self.dfs(nums, [], results)
        
        return results
    
    def dfs(self, nums, curr, results):
        if not nums and curr not in results:
            results.append(curr)
            return
        
        for i in nums:
            new_nums = list(nums)
            new_nums.remove(i)
            self.dfs(new_nums, curr + [i], results)