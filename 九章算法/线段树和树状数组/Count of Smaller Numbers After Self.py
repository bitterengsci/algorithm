'''
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property 
where counts[i] is the number of smaller elements to the right of nums[i].

Example 1
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Example 2
Input: [1, 2, 3, 4]
Output: [0, 0, 0, 0]
'''

class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def countSmaller(self, nums):
        # write your code here
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            update(rank[x])
        return res[::-1]