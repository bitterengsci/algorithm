#-*-coding:utf-8-*-
'''
    Description
    Given an array of n integers, and a moving window(size k),
    move the window at each iteration from the start of the array,
    find the sum of the element inside the window at each moving.
'''
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        res = []

        if nums is None or nums == [] or len(nums) < k or k < 0:
            return res

        i, j = 0, k
        res.append(sum(nums[i:j]))

        while j < len(nums):
            i += 1
            j += 1
            res.append(res[-1] - nums[i - 1] + nums[j - 1])
            # res.append(sum(nums[i:j]))  # 会造成 Time Limit Exceeded

        return res
