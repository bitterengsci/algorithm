#-*-coding:utf-8-*-
'''
Description
    Given a string s and a string t, check if s is subsequence of t.

    You may assume that there is only lower case English letters in both s and t.
    t is potentially a very long (length ~= 500,000) string, and s is a short string (length <= 100).

    A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
    of the characters without disturbing the relative positions of the remaining characters.
    (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Challenge
    If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B,
    and you want to check one by one to see if T has its subsequence.
    In this scenario, how would you change your code?
'''
class Solution:
    """
    @param s: the given string s
    @param t: the given string t
    @return: check if s is subsequence of t
    """

    def isSubsequence(self, s, t):

        if len(s) == 0:
            return True

        for i in range(len(t)):
            if s[0] == t[i]:
                s = s[1:]
            if len(s) == 0:
                return True

        return False

    def isSubsequence2(self, s, t):

        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        if i == len(s):
            return True
        else:
            return False
