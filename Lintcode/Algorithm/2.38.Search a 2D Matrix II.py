#-*-coding:utf-8-*-
'''
Given a big sorted array with positive integers sorted by ascending order.
The array is so big so that you can not get the length of the whole array directly,
and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).
Find the first index of a target number.
Your algorithm should be in O(log k), where k is the first index of the target number.
Return -1, if the number doesn't exist in the array.

Note
    从左下角开始，往右上角逼近
'''


class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix[0] == []:
            return 0

        row, column = len(matrix), len(matrix[0])

        i, j = row - 1, 0

        occurrence = 0
        while i >= 0 and j < column:
            if matrix[i][j] == target:
                occurrence += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return occurrence

