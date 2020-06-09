class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    
    # Approach: 递推, 循环
    def fibonacci1(self, n):
        fib = [0, 0, 1]
        for i in range(3, n + 1, 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]
    
    # Approach: 递推, 循环 + 滚动数组
    def fibonacci2(self, n):
        fib = [0, 1]
        for i in range(2, n + 1, 1):
            fib[i % 2] = fib[0] + fib[1]
        return fib[(n + 1) % 2]
        
    # Approach: 递归 (TLE)
    # def dfs(self, n):
    #     if n <= 2:
    #         return n - 1
    #     return self.dfs(n - 1) + self.dfs(n - 2)
    
    # def fibonacci(self, n):
    #     return self.dfs(n)
        
    # Approach: 递归 + 记忆化搜索
    def dfs(self, n, fib):
        if fib[n] != -1:
            return fib[n]
        if n <= 2:
            fib[n] = n - 1
            return fib[n]
        fib[n] = self.dfs(n - 1, fib) + self.dfs(n - 2, fib)
        return fib[n]
    
    def fibonacci(self, n):
        result = [-1] * (n + 1)
        self.dfs(n, result)
        return result[n]


    # 矩阵快速幂
    def quickPow(self, a, n):
        base = a
        resultMatrix = Matrix(2, 2)
        resultMatrix.numbers[0][0] = 1
        resultMatrix.numbers[1][1] = 1
        while n > 0:
            if n % 2 == 1:
                resultMatrix = resultMatrix.multiply(base)
            base = base.multiply(base)
            n //= 2
        return resultMatrix
    
    def fibonacci(self, n):
        if n == 1:
            return 0
        
        startMatrix = Matrix(2, 1)
        rollingMatrix = Matrix(2, 2)
        
        startMatrix.numbers[0][0] = 1
        startMatrix.numbers[1][0] = 0
        rollingMatrix.numbers[0][0] = 1
        rollingMatrix.numbers[0][1] = 1
        rollingMatrix.numbers[1][0] = 1
        rollingMatrix.numbers[1][1] = 0
        rollingMatrix = self.quickPow(rollingMatrix, n - 2)
        startMatrix = rollingMatrix.multiply(startMatrix)
        
        return startMatrix.numbers[0][0]

class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.numbers = []
        for i in range(0, row, 1):
            self.numbers.append([0] * column)
        
    def multiply(self, a):
        newMatrix = Matrix(self.row, a.column)
        for i in range(0, newMatrix.row, 1):
            for j in range(0, newMatrix.column, 1):
                for k in range(0, newMatrix.column, 1):
                    newMatrix.numbers[i][j] = newMatrix.numbers[i][j] + self.numbers[i][k] * a.numbers[k][j]
        return newMatrix