#-*-coding:utf-8-*-
'''
Description

    Given n books and the i-th book has pages[i] pages. There are k persons to copy these books.

    These books list in a row and each person can claim a continous range of books.
    For example, one copier can copy the books from i-th to j-th continously,
    but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

    They start copying books at the same time and they all cost 1 minute to copy 1 page of a book.
    What's the best strategy to assign books so that the slowest copier can finish at earliest time?

    Return the shortest time that the slowest copier spends.

Challenge
    O(nk) time
'''

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer

    可以使用二分或者动态规划解决这道题目. 不过更推荐二分答案的写法, 它更节省空间, 思路简洁, 容易编码.

    对于假定的时间上限 tm 我们可以使用贪心的思想判断这 k 个人能否完成复印 n 本书的任务:
            将尽可能多的书分给同一个人, 判断复印完这 n 本书需要的人数是否不大于 k 即可.

    而时间上限 tm 与可否完成任务(0或1)这两个量之间具有单调性关系, 所以可以对 tm 进行二分查找, 查找最小的 tm, 使得任务可以完成.
    """


    # Binary Search
    def copyBooks_bs(self, pages, k):
        n = len(pages)
        if n == 0:
            return 0
        l = max(pages)
        r = sum(pages)
        while l < r:
            mid = (l + r) // 2
            if self.ok(pages, k, mid):
                r = mid
            else:
                l = mid + 1
        return l

    def ok(self, pages, k, tm):
        num = 1
        pageSum = 0
        for i in pages:
            if pageSum + i <= tm:
                pageSum += i
            else:
                num += 1
                pageSum = i
        return num <= k



    # DP
    def copyBooks_dp(self, pages, k):
        n = len(pages)
        if k > n:
            k = n

        if n == 0:
            return 0

        sum = [0] * n
        sum[0] = pages[0]
        for i in range(1, n):
            sum[i] = sum[i - 1] + pages[i]

        f = [[0] * k for _ in range(n)]

        for i in range(n):
            f[i][0] = sum[i]

        for j in range(1, k):
            p = 0
            f[0][j] = pages[0]
            for i in range(1, j):
                f[i][j] = max(f[i - 1][j], pages[i])

            for i in range(j, n):
                while p < i and f[p][j - 1] < sum[i] - sum[p]:
                    p += 1
                f[i][j] = max(f[p][j - 1], sum[i] - sum[p])
                if p > 0:
                    p -= 1
                f[i][j] = min(f[i][j], max(f[p][j - 1], sum[i] - sum[p]))
        return f[n-1][k-1]


class Solution2:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer


    使用九章算法强化班中讲过的基于答案值域的二分法。
    答案的范围在 max(pages)~sum(pages) 之间，每次二分到一个时间 time_limit 的时候，
    用贪心法从左到右扫描一下 pages，看看需要多少个人来完成抄袭。
    如果这个值 <= k，那么意味着大家花的时间可能可以再少一些，如果 > k 则意味着人数不够，需要降低工作量。

    时间复杂度 O(nlog(sum))O(nlog(sum)) 是该问题时间复杂度上的最优解法
    """

    def copyBooks(self, pages, k):
        if not pages:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.get_least_people(pages, mid) <= k:
                end = mid
            else:
                start = mid

        if self.get_least_people(pages, start) <= k:
            return start

        return end

    def get_least_people(self, pages, time_limit):
        count = 0
        time_cost = 0
        for page in pages:
            if time_cost + page > time_limit:
                count += 1
                time_cost = 0
            time_cost += page

        return count + 1


s = Solution()
print(s.copyBooks_bs([3, 2, 4], 3))
print(s.copyBooks_dp([3, 2, 4], 3))

s = Solution2()
print(s.copyBooks([3, 2, 4], 3))
