class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    # 0 1 1 2 3 5 8 13 21 44 63
    def fibonacci(self, n):   # index 0 ~ n-1
        if n == 1:
            return 0
            
        f = [0, 1]
        
        now = 1
        for i in range(1, n):
            f[now] = f[now] + f[1 - now]
            now = 1 - now
        
        return f[1 - now]