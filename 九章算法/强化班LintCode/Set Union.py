'''
Description
There is a list composed by sets. If two sets have the same elements, merge them. 

The number of sets n <=1000.
The number of elements for each set m <= 100.
The element must be a non negative integer and not greater than 100000.

Example 1:
Input: list = [[1,2,3],[3,9,7],[4,5,10]]
Output: 2
Explanation: There are 2 sets of [1,2,3,9,7] and [4,5,10] left.

Example 2:
Input: list = [[1],[1,2,3],[4],[8,7,4,5]]
Output: 2
Explanation: There are 2 sets of [1,2,3] and [4,5,7,8] left.
'''

class Solution:
    """
    @param sets: Initial set list
    @return: The final number of sets
    """
    def find(self, x, f):
        if x != f[x]:
            f[x] = self.find(f[x], f)
        return f[x]

    def setUnion(self, sets):
        f = {}
        for s in sets:
            first = s[0]
            for x in s:
                if not f.has_key(x):
                    f[x] = first
                else:
                    fFirst = self.find(first, f)
                    fx = self.find(x, f)
                    if fx != fFirst:
                        f[fx] = fFirst
        for s in sets:
            for x in s:
                self.find(x, f)
        hashSet = {}
        n = 0
        for val in f.values():
            if not hashSet.has_key(val):
                n += 1
                hashSet[val] = val
        return n