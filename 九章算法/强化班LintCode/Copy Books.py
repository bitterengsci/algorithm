# 基于答案值域的二分法
# 答案的范围在 max(pages)~sum(pages) 之间，
# 每次二分到一个时间 time_limit 的时候，用贪心法从左到右扫描一下 pages，看看需要多少个人来完成抄袭
# 如果这个值 <= k，那么意味着大家花的时间可能可以再少一些，如果 > k 则意味着人数不够，需要降低工作量

# 时间复杂度 O(nlog(sum)), 是该问题时间复杂度上的最优解法

def copyBooks(self, pages, k):
        if not pages: return 0
            
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
                while (p < i and f[p][j - 1] < sum[i] - sum[p]):
                    p += 1
                f[i][j] = max(f[p][j - 1], sum[i] - sum[p])
                if p > 0:
                    p -= 1
                f[i][j] = min(f[i][j], max(f[p][j - 1], sum[i] - sum[p]))
        return f[n-1][k-1]


    # My ans
    def copyBooks_myans(self, pages, k):
        if not pages: return 0
        
        start, end = max(pages), sum(pages)
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if self.can_finish_copy(pages, k, mid):
                end = mid
            else:
                start = mid
    
        if self.can_finish_copy(pages, k, start):
            return start
        else:
            return end
    
    def can_finish_copy(self, pages, k, time):
        p = 0   # index of array pages
        t = time
        while p < len(pages):
            if t >= pages[p]:
                t -= pages[p]
            else:
                k -= 1
                t = time - pages[p]
            p += 1
            
        return k > 0  # 不能用 k >= 0