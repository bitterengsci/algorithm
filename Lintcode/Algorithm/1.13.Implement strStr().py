''' 
库函数实现题
C strstr() Java indexOf() Python find()

For a given source string and a target string, you should output the first index(from 0) of target string in source string.
If target does not exist in source, just return -1.

Challenge: O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)
'''
class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        if not target:
            return 0
             
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if target[j] != source[i + j]:
                    break
                if j == len(target) - 1:
                    return i
        return -1