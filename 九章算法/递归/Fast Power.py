class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    
    # Approach: 递归
    def fastPower1(self, a, b, n):
        
        mod = 1
        
        while n > 0:
            n -= 1
            mod *= a
            mod %= b
            
        return mod % b
        
    # Approach: 二分, 递归
    def fastPower2(self, a, b, n):
        if n == 0:
            return 1 % b
        
        if n % 2:
            return (a * self.fastPower(a, b, n//2) ** 2) % b 
        else:
            return (self.fastPower(a, b, n//2) ** 2 ) % b 
        
    # Approach: 二分, 递归 + 记忆化搜索
    def dfs(self, a, b, n):
        if n not in self.memo:
            if n % 2:
                self.memo[n] = (a * self.fastPower(a, b, n//2) ** 2) % b 
            else:
                self.memo[n] =  (self.fastPower(a, b, n//2) ** 2 ) % b
        
    def fastPower(self, a, b, n):
        self.memo = {0: 1 % b}
        
        self.dfs(a, b, n)
        
        print(self.memo)
            
        return self.memo[n]