# -*-coding:utf-8-*-
'''
Description
There is an integer array which has the following features:
    The numbers in adjacent positions are different.    (避免类似 [1 2 2 1] 无峰的情况)
    A[0] < A[1] && A[A.length - 2] > A[A.length - 1].
We define a position P is a peak if:
    A[P] > A[P-1] && A[P] > A[P+1]       (先增后减数组, 一定有peak(局部最大))

Find a peak element in this array. Return the index of the peak.

Note
找所有peak → for循环, O(n)
找一个peak → 非排序数组如何二分?
四种情况  mid-1<mid<mid+1 (递减区间, 左半部分一定有峰)
         mid-1>mid>mid+1 (有半部分一定有峰)
         mid > mid-1 & mid+1 (mid就是峰, return it)
         mid < mid-1 & mid+1 (左右两边都至少存在一个解)
'''


class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """

    def findPeak(self, A):
        if len(A) == 0:
            return None

        start, end = 0, len(A) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2

            if mid == 0:
                pre, next = A[mid], A[mid + 1]
            elif mid == len(A):
                pre, next = A[mid - 1], A[mid]
            else:
                pre, next = A[mid - 1], A[mid + 1]

            A_mid = A[mid]

            if A_mid > pre and A_mid > next:
                return mid
            elif pre < A_mid < next:
                start = mid
            # elif pre > A_mid > next:
            #     end = mid
            # else:
            #     end = mid    # or start = mid (does not matter)
            else:
                end = mid

        def findPeak2(self, A):
            if len(A) == 0:
                return None

            start, end = 1, len(A) - 2

            while start + 1 < end:
                mid = start + (end - start) // 2

                if A[mid] > A[mid - 1]:
                    start = mid
                # elif A[mid] < A[mid+1]:
                #     end = mid
                else:
                    end = mid

            if A[start] > A[end]:
                return start
            return end
