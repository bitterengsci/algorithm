class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    # Insight: create另一个set/list, 在循环中可以删除 (因为for-loop的iterator在循环中不可以改变, 否则会出错)
    def longestConsecutive(self, num):
        nums = []            # nums = set()
        for i in num:
            nums.append(i)   # nums.add(i)

        ans = 0
        for x in num:      # input array
            if x in nums:  # hashset
                length = 1
                nums.remove(x)
                # search its consecutives
                left, right = x - 1, x + 1  
                while left in nums:
                    nums.remove(left)
                    left -= 1
                    length += 1
                while right in nums:
                    nums.remove(right)
                    right += 1
                    length += 1
                    
                ans = max(ans, length)
        return ans