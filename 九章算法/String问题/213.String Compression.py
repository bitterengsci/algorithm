#-*-coding:utf-8-*-
'''
Description
    Implement a method to perform basic string compression using the counts of repeated characters.
    For example, the string aabcccccaaa would become a2b1c5a3.

    If the "compressed" string would not become smaller than the original string,
    your method should return the original string.
    You can assume the string has only upper and lower case letters (a-z).
'''
class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """

    def compress(self, originalString):
        i = 0
        newString = ""
        while i < len(originalString):
            count = 0
            while count < len(originalString) - i and originalString[i] == originalString[i + count]:
                count += 1
            newString += originalString[i] + str(count)
            i += count

        if len(newString) >= len(originalString):
            return originalString

        return newString
