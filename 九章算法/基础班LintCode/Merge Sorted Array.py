class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    
    # Approach: 设置i和j双指针, 分别从两个数组的尾部想头部移动, 并判断Ai和Bj的大小关系, 从而保证最终数组有序, 同时每次index从尾部向头部移动
    def mergeSortedArray1(self, A, m, B, n):
        if not B:
            return
        
        # if not A:
        #     A = B
        #     return
        
        i, j = m - 1, n - 1  # two pointers
        idx = m + n - 1
        
        # swap
        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[idx] = B[j]
                j -= 1
                idx -= 1
            else:
                A[idx] = A[i]
                i -= 1
                idx -= 1
                
        if j >= 0:
            A[:j+1] = B[:j+1]
    
    # Approach: merge and then swap (TLE)       
    def mergeSortedArray(self, A, m, B, n):
        if not B: return
        
        A[-n:] = B # copy B to the end of A
        
        idx = 0
        
        # bubble sort (swap)
        # Traverse through all array elements 
        for i in range(m + n - 1): 
        # range(n) also work but outer loop will repeat one time more than needed.
            # Last i elements are already in place 
            for j in range(0, m + n - i - 1): 
                # traverse the array from 0 to n-i-1 
                # Swap if the element found is greater than the next element 
                if A[j] > A[j+1] : 
                    A[j], A[j+1] = A[j+1], A[j] 

        