class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        results = []
        self.dfs(sorted(candidates), 0, [], target, results)
        return results
    
    def dfs(self, candidates, idx, curr, target, results):
        if target == 0 and curr not in results:
            results.append(curr)
            return
        
        if idx == len(candidates): return
        
        if target >= candidates[idx]:
            self.dfs(candidates, idx, curr + [candidates[idx]], target - candidates[idx], results)
            self.dfs(candidates, idx+1, curr + [candidates[idx]], target - candidates[idx], results)
        
        # self.dfs(candidates, idx, curr, target, results)
        self.dfs(candidates, idx+1, curr, target, results)