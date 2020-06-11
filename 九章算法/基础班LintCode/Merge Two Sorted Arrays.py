class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1
                
        if i != len(A):
            res += A[i:]
            
        if j != len(B):
            res += B[j:]
        
        return res

# Follow-Up: How can you optimize your algorithm if one array is very large and the other is very small?

# my ans: insert small array into the large one, record at which index to insert and copy once.