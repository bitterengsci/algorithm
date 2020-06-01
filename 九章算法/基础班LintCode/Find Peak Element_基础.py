class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """


    # 二分答案
    def findPeak(self, A):
        
        start, end = 1, len(A) - 2   # index 0 and -1 cannot be the ans
        
        while start + 1 < end:
            mid = start + (end - start) // 2 
            
            if A[mid] < A[mid + 1]:
                start = mid
            else:
                end = mid

        if A[start] > A[end]:
            return start
        else:
            return end