class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        
        mapping = {}
        for word in strs:
            sortedword = ''.join(sorted(word))  # sort the word alphabetically
            mapping[sortedword] = [word] if sortedword not in mapping else mapping[sortedword] + [word]
        
        res = []
        for key in mapping:
            if len(mapping[key]) >= 2:
                res += mapping[key]
        
        return res
