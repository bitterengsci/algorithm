#-*-coding:utf-8-*-
'''
给一个字符串，代表时间，如"12:34"（这是一个合法的输入数据），并找到它的下一次不重复(不存在相同的数字)的时间。
如果它是最大的时间"23:59"，那么返回的答案是最小的"01:23"。如果输入是非法的，则返回-1
'''


class Solution:
    """
    @param time:
    @return: return a string represents time
    """

    def nextTime(self, time):
        if len(time) != 5 or time is None:
            return "-1"
        ans = ""
        temp = time.split(":")
        hour, mins = int(temp[0]), int(temp[1])
        nowtime = hour * 60 + mins
        if hour >= 24 or mins >= 60:
            return "-1"

        digit = [600, 60, 10, 1]
        for i in range(1, 1440):     # 1 day = 1440 mins
            nexttime = (nowtime + i) % 1440
            ans = ""
            print('next time = ', nexttime)
            for j in range(4):
                ans += str(nexttime // digit[j])
                print('ans = ', ans)
                nexttime %= digit[j]
                print('next time = ', nexttime)
            # if self.isUnique(ans):
            #     break
            if list(ans) != set(ans):
                break
        return ans[0: 2] + ":" + ans[2:]

    def isUnique(self, string):
        print(string)
        if len(string) == 0:
            return False
        Set = set()
        for i in range(len(string)):
            if string[i] in Set:
                return False
            Set.add(string[i])
        return True

s = Solution()
print(s.nextTime("12:34"))
