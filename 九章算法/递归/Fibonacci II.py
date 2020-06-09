class Matrix:
	def __init__(self, matrix):
		self.mat = matrix
		
	def __mul__(self, m):
		product = Matrix([[0, 0], [0, 0]])
		for i in range(2):
			for k in range(2):
				if self.mat[i][k] == 0:
					continue
				for j in range(2):
					product.mat[i][j] += self.mat[i][k] * m.mat[k][j]
					product.mat[i][j] %= 10000
		return product

class Solution:
    """
    @param n: an integer
    @return: return a string
    """
    def lastFourDigitsOfFn(self, n):
        if n == 0: return 0
        
        A = Matrix([[1, 1], [1, 0]])
        m = self.power(A, n - 1)
        
        return m.mat[0][0]
        
    def power(self, A, a):
        B = Matrix([[1, 0], [0, 1]])

        while a > 0:
            if a % 2 == 1:
                B = B * A
            A = A * A
            a //= 2
        
        return B


# SideNote: Python中list的mutable属性, 什么时候是指向reference, 什么时候是deepcopy, 需要区分!