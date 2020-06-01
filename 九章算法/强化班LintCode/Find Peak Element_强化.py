'''
There is an integer array which has the following features:
The numbers in adjacent positions are different.
A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peak if: A[P] > A[P-1] && A[P] > A[P+1]
Find a peak element in this array. Return the index of the peak.

Example 1:
	Input:  [1, 2, 1, 3, 4, 5, 7, 6]
	Output:  1 or 6
	Explanation: return the index of peek.

Example 2:
	Input: [1,2,3,4,1]
	Output:  3
'''

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
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