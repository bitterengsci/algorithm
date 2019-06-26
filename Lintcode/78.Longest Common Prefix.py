#-*-coding:utf-8-*-
'''
Description
    Given k strings, find the longest common prefix (LCP).
'''
class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        prefix = ""

        if strs == []:
            return prefix

        if len(strs) == 1:
            return strs[0]

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            if all(strs[0][i] == s[i] for s in strs[1:]):
                prefix += strs[0][i]

        return prefix

    def longestCommonPrefix2(self, strs):
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""

        end, minl = 0, min([len(s) for s in strs])
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i - 1][end]:
                    return strs[0][:end]
            end += 1

        return strs[0][:end]
