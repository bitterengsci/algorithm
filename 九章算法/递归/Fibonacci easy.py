from functools import lru_cache
class Solution:
    """
    @param n: an integer
    @return: an integer f(n)
    """
    @lru_cache(maxsize=10000)
    def fibonacci(self, n):
        if n == 1:
            return 0
        elif n in [2, 3]:
            return 1
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)