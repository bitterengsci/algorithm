#-*-coding:utf-8-*-
'''
Description

    Given a big sorted array with non-negative integers sorted by non-decreasing order.
    The array is so big so that you can not get the length of the whole array directly,
    and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++).

    Find the first index of a target number.
    Your algorithm should be in O(log k), where k is the first index of the target number.

    Return -1, if the number doesn't exist in the array.

Challenge
    O(logn) time, n is the first index of the given target number.

Notice:
    If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2147483647.
'''

"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):

        k = self.getK(reader, target, 1)

        if k == 1:
            if reader.get(0) == target:
                return 0
            if reader.get(1) == target:
                return 1
            return -1

        start, end = k // 2, k
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid

        if reader.get(start) == target:
            return start

        if reader.get(end) == target:
            return end

        return -1

    def getK(self, reader, target, k):

        if reader.get(k) >= target:
            return k
        else:
            return self.getK(reader, target, 2 * k)
