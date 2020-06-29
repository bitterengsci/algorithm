class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute_recursion(self, nums):
        results = []
        
        self.dfs(nums, [], results)
        
        return results
    
    def dfs(self, nums, curr, results):
        if not nums:
            results.append(curr)
            return
        
        for i in nums:
            new_nums = list(nums)
            new_nums.remove(i)
            self.dfs(new_nums, curr + [i], results)
            
    
    def permute2(self, nums):
        def _permute(result, temp, nums):
            if nums == []:
                result += [temp]
            else:
                for i in range(len(nums)):
                    _permute(result, temp + [nums[i]], nums[:i] + nums[i+1:])

        if nums is None:
            return []
        
        if nums is []:
            return [[]]

        result = []
        _permute(result, [], sorted(nums))
        return result

    # Non-Recursion
    # 手动模拟栈
    def permute_non_recursion(self, nums):
        if nums is None: return []
        if nums == []: return [[]]
        
        nums = sorted(nums)
        permutation = []
        stack = [-1]    # to store indices
        permutations = []
        
        while len(stack):  # [1, 2, 3], len=3
            # print(permutation, permutations, stack)
            index = stack.pop()
            index += 1    # 0
            # 退
            while index < len(nums):   #
                if nums[index] not in permutation:
                    break
                index += 1
            else:
                if len(permutation):
                    permutation.pop()
                continue
                
            # 进
            stack.append(index)
            stack.append(-1)   # [0, -1]
            permutation.append(nums[index])   # [1]
            
            if len(permutation) == len(nums):
                print(permutation, "stack=", stack)
                permutations.append(list(permutation))  # deep copy [1, 2, 3]
                
        return permutations

Solution().permute_non_recursion([1, 2, 3])