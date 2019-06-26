#-*-coding:utf-8-*-
'''
Description

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A
so that the result equals B.

    1.0 <= A.length <= 20000
    2.0 <= A.length <= 20000
    3.A and B consist only of lowercase letters.
'''
class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """

    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False

        element = []
        diff = []
        duplicate = False
        for i in range(len(A)):
            if A[i] in element:
                duplicate = True
            element.append(A[i])
            if A[i] != B[i]:
                diff.append(i)

        if len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
            return True

        if len(diff) == 0 and duplicate:
            return True

        return False

    def buddyStrings2(self, A, B):
        if len(A) != len(B):
            return False
        print(set(A))
        if A == B and len(set(A)) < len(A):
            return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]

        print(dif)
        print(dif[1][::-1])      # [::-1] equals slicing from : to -1
        return len(dif) == 2 and dif[0] == dif[1][::-1]

s = Solution()
# print(s.buddyStrings('ab', 'ab'))
print(s.buddyStrings2('abcd', 'abdc'))
