class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
       
        results = []
        
        self.dfs(sorted(num), 0, [], target, results)
        
        return results
       
    def dfs(self, num, idx, curr, target, results):
        if target == 0 and curr not in results:
            results.append(curr)
            return
        
        if idx == len(num):
            return
        
        if target >= num[idx]:
            self.dfs(num, idx + 1, curr, target, results)
            self.dfs(num, idx + 1, curr + [num[idx]], target - num[idx], results)
