class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition_myans(self, s):
        results = []
        
        self.dfs(s, 0, [], results)
        return results
    
    def dfs(self, s, idx, curr, results):
        if not s:
            results.append(curr)
            return
        
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                self.dfs(s[i:], i, curr + [s[:i]], results)
    
    def is_palindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
        # return s == s[::-1]
        
        
    # 记忆化搜索
    def partition(self, s):
        return self.dfs_memo(s, {})
        
    def dfs_memo(self, s, memo):
        if s == "":
            return []
        if s in memo:
            return memo[s]
            
        partitions = []
        for i in range(len(s) - 1):
            prefix = s[:i + 1]
            if prefix != prefix[::-1]:
                continue
            
            sub_partitions = self.dfs_memo(s[i + 1:], memo)
            for p in sub_partitions:
                partitions.append([prefix] + p)
                
        if s == s[::-1]:
            partitions.append([s])
        
        memo[s] = partitions
        return partitions
    
    """
    如何优化?
    - 用hashmap存储回文串, 但这样没效果
        getkey不是 O(1), 是O(size of key), 取决于用作key的字符串有多长..
    - 用二维数组
    """