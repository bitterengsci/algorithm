#-*-coding:utf-8-*-
'''
Description
    Given an array of integers, find two numbers such that they add up to a specific target number.

    The function twoSum should return indices of the two numbers such that they add up to the target,
    where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

    You may assume that each input would have exactly one solution

Challenge
    Either of the following solutions are acceptable:
    O(n) Space, O(nlogn) Time
    O(n) Space, O(n) Time
'''
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    # HashMap
    def twoSum(self, numbers, target):
        dic = dict()

        for i in range(len(numbers)):
            if target - numbers[i] in dic.keys():
                return [dic[target - numbers[i]], i]
            dic[numbers[i]] = i

    # Sort and 2 pointers
    # (若不需要return index, 只需要return满足target的数值, 则额外空间为O(1))
    def twoSum(self, numbers, target):
        numbers.sort()
        i, j = 0, len(numbers) - 1

        while i != j:
            if numbers[i] + numbers[j] > target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                return i, j
