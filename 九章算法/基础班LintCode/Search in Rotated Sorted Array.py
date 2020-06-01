'''
4 5 6 7 0 1 2       target=6
    o o x x o o o      (not ooxx的形式)
    → 方法一: 找到o/找最小 O(logn), 然后还原成 ooxx, 但还原操作O(n), 不行
    → 方法二: start ≤ target ≤ mid 答案在左边;  target > mid && target < start 答案在右边

二分思想要求, 去掉一半后, 剩下的一半必须还是刚开始的构型。
        → 二分之后必须还是RSA (SA⊆RSA)
'''
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if target >= A[mid] > A[start] or A[mid] > A[start] > target or A[start] >= target > A[mid]:
                start = mid
            if A[mid] > target >= A[start] or target >= A[start] > A[mid] or A[start] > A[mid] >= target:
                end = mid

        if A[start] == target:
            return start
        elif A[end] == target:
            return end
        return -1