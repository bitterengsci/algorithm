class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    # Approach: search in rows, then search column in one row
    def searchMatrix_row_col(self, matrix, target):
        if not matrix or not matrix[0]: return False
        
        R, C = len(matrix), len(matrix[0])
        
        # search in rows
        start, end = 0, R - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target < matrix[mid][-1]:
                end = mid
            else:
                start = mid
        
        if matrix[start][-1] < target:
            target_row = end
        else:
            target_row = start
        
        # search column in one row
        start, end = 0, C - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if target < matrix[target_row][mid]:
                end = mid
            else:
                start = mid
                
        return matrix[target_row][start] == target or matrix[target_row][end] == target
        

    # Approach: do it in one pass, treat it as 1D array
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        
        R, C = len(matrix), len(matrix[0])
        
        start, end = 0, R * C - 1
        while start + 1 < end:
            mid = (start + end) // 2
            x, y = mid // C, mid % C
            if matrix[x][y] < target:
                start = mid
            else:
                end = mid

        return matrix[start // C][start % C] == target or matrix[end // C][end % C] == target
        