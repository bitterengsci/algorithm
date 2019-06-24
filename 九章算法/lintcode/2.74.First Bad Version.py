'''
Description

The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case,
so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one.
The details interface can be found in the code's annotation part.
'''
# class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # write your code here
        start, end = 1, n

        while start + 1 < end:
            mid = start + (end - start) // 2
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

        if SVNRepo.isBadVersion(start):
            return start
        return end
