#-*-coding:utf-8-*-
'''
Description
Given a big sorted array with positive integers sorted by ascending order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by ArrayReader.get(k) (or ArrayReader->get(k) for C++). Find the first index of a target number. Your algorithm should be in O(log k), where k is the first index of the target number.

Return -1, if the number doesn’t exist in the array.

Notice:
If you accessed an inaccessible index (outside of the array), ArrayReader.get will return 2147483647.
'''

