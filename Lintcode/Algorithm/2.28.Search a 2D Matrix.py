#-*-coding:utf-8-*-
'''
Description
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Challenge O(log(n) + log(m)) time

Note:
    不是二分法，但是是常考题

'''
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMatrix(self, matrix, target):

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        # search in rows
        start, end = 0, m - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target < matrix[mid][-1]:
                end = mid
            else:
                start = mid

        if matrix[start][-1] < target:
            target_m = end
        else:
            target_m = start

        # search in one row (the row of target_m)
        start, end = 0, n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target < matrix[target_m][mid]:
                end = mid
            else:
                start = mid

        if matrix[target_m][start] == target or matrix[target_m][end] == target:
            return True

        return False

    def searchMatrix2(self, matrix, target):
        if len(matrix) == 0:
            return False

        n, m = len(matrix), len(matrix[0])

        start, end = 0, n * m - 1

        while start + 1 < end:
            mid = (start + end) // 2
            print(mid)
            x, y = mid // m, mid % m
            print(x, y)
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid

        x, y = start // m, start % m
        if matrix[x][y] == target:
            return True

        x, y = end // m, end % m
        if matrix[x][y] == target:
            return True

        return False


if "__main__" == __name__:
    s = Solution()
    mat = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    s.searchMatrix2(mat, 3)
