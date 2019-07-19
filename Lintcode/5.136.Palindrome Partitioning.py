#-*-coding:utf-8-*-
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """

    def partition(self, s):
        results = []
        self.dfs(s, 0, [], results)
        return results

    def dfs(self, s, startIndex, partition, results):
        if startIndex == len(s):
            results.append(list(partition))  # deepcopy

        for i in range(startIndex, len(s)):
            print(i)

            substring = s[startIndex: i+1]
            print('substring', substring)
            if not self.isPalindrome(substring):
                continue

            partition.append(substring)
            if i < len(s):
                self.dfs(s, i+1, partition, results)
            partition.pop(-1)

    def isPalindrome(self, s):
        # 一头一尾两个指针, 头尾两个指针往中间靠, 一个++, 一个--
        # for (int i=0, j=s.length()-1; i<j; i++, j--)

        # 优化
        # 用hashmap存储回文串, 但这样没效果
        # getkey不是 O(1), 是O(size of key), 取决于用作key的字符串有多长..
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    # def getIsPalindrome(self, s):
    #     n = len(s)
    #     isPalindrome = [[False for _ in range(n)] for _ in range(n)]

    #     for i in range(n):
    #         isPalindrome[i][i] = True

    #     for i in range(n):
    #         isPalindrome[i][i + 1] = (s[i] == s[i + 1])

    #     for i in reversed(range(n-3)):
    #         for j in range(i+2, n):
    #             isPalindrome[i][j] = isPalindrome[i + 1][j - 1] and s[i] == s[j]

    #     return isPalindrome


'''
    九章算法其他方法
'''
class Solution_1:
    # 使用 append + pop 的方式
    def partition(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            results.append(list(stringlist))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                stringlist.append(prefix)
                self.dfs(s[i:], stringlist, results)
                stringlist.pop()

    def is_palindrome(self, s):
        return s == s[::-1]

class Solution_2:
    # 记忆化搜索来实现 get_is_palindrome
    def partition(self, s):
        results = []
        self.dfs(s, 0, [], {}, results)
        return results

    def generate_solution(self, s, partition):
        strings = []
        last_index = -1
        for i in partition:
            strings.append(s[last_index + 1: i + 1])
            last_index = i
        return strings

    def get_is_palindrome(self, memo, s, i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == j:
            return True
        if i + 1 == j:
            return s[i] == s[j]

        memo[(i, j)] = s[i] == s[j] and self.get_is_palindrome(memo, s, i + 1, j - 1)
        return memo[(i, j)]

    def dfs(self, s, index, partition, memo, results):
        if index == len(s):
            results.append(self.generate_solution(s, partition))
            return

        for i in range(index, len(s)):
            if not self.get_is_palindrome(memo, s, index, i):
                continue
            partition.append(i)
            self.dfs(s, i + 1, partition, memo, results)
            partition.pop()


class Solution_3:
    # 使用了动态规划优化的
    def partition(self, s):
        results = []
        is_palindrome = self.get_is_palindrome(s)
        self.dfs(s, 0, [], is_palindrome, results)
        return results

    def generate_solution(self, s, partition):
        strings = []
        last_index = -1
        for i in partition:
            strings.append(s[last_index + 1: i + 1])
            last_index = i
        return strings

    def dfs(self, s, index, partition, is_palindrome, results):
        if index == len(s):
            results.append(self.generate_solution(s, partition))
            return

        for i in range(index, len(s)):
            if not is_palindrome[index][i]:
                continue
            partition.append(i)
            self.dfs(s, i + 1, partition, is_palindrome, results)
            partition.pop()

    def get_is_palindrome(self, s):
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(n - 1):
            is_palindrome[i][i + 1] = (s[i] == s[i + 1])

        for delta in range(2, n):
            for i in range(n - delta):
                j = i + delta
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]

        return is_palindrome


class Solution_4:
    # 使用记忆化搜索来做的办法，和 word break ii 类似
    def partition(self, s):
        return self.dfs(s, {})

    def dfs(self, s, memo):
        if s == "":
            return []
        if s in memo:
            return memo[s]

        partitions = []
        for i in range(len(s) - 1):
            prefix = s[:i + 1]
            if prefix != prefix[::-1]:
                continue

            sub_partitions = self.dfs(s[i + 1:], memo)
            for p in sub_partitions:
                partitions.append([prefix] + p)

        if s == s[::-1]:
            partitions.append([s])

        memo[s] = partitions
        return partitions
