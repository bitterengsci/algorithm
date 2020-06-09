# 给定一个数n，返回该数的二阶阶乘。
# 在数学中，正整数的二阶阶乘表示不超过这个正整数且与它有相同奇偶性的所有正整数乘积

class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def doubleFactorial(self, n):
        if n <= 0 or n > 33:
            return -1
        
        if n == 1 or n == 2:   # n <= 3
            return n
        else:
            return n * self.doubleFactorial(n - 2)