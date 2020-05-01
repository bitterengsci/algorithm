#-*-coding:utf-8-*-
'''
Description
    Compare two version numbers version1 and version2.
    If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

    You may assume that the version strings are non-empty and contain only digits and the . character.
    The . character does not represent a decimal point and is used to separate number sequences.
    For instance, 2.5 is not "two and a half" or "half way to version three",
    it is the fifth second-level revision of the second first-level revision.
'''
class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """

    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")

        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1

        return 0

    def compareVersion2(self, version1, version2):
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        for i in range(max(len(v1_list), len(v2_list))):
            v1 = int(v1_list[i]) if len(v1_list) > i else 0
            v2 = int(v2_list[i]) if len(v2_list) > i else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
