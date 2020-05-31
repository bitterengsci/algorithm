'''
There is an integer matrix which has the following features:
The numbers in adjacent positions are different.
The matrix has n rows and m columns.
    For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
    For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if:
A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] > A[j][i-1]

Find a peak element in this matrix. Return the index of the peak.

Example
    Given a matrix:
    [
    [1 ,2 ,3 ,6 ,5],
    [16,41,23,22,6],
    [15,17,24,21,7],
    [14,18,19,20,10],
    [13,14,11,10,9]
    ]
    return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Challenge
    Solve it in O(n+m) time.
    If you come up with an algorithm that you thought it is O(n log m) or O(m log n), 
    can you prove it is actually O(n+m) or propose a similar but O(n+m) algorithm?

和在数组中find peak element一样，对行和列分别进行二分查找。
* 先对行进行二分搜索，对搜到的那一行元素再进行二分搜索寻找peak element
* 对找到的element看上下行的同列元素，若相同则返回，若比上小则在上半部分行继续进行搜索，若比下小则在下半部分的行继续进行搜索
'''

### TODO


def findPeakII(A):

    # 根据题意，第1行和最后一行都不可能是peak，所以从第2行和倒数第2行开始
    low = 1, high = len(length) - 2

