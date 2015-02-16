# coding=utf-8

class Solution_initial:
    def findPeakElement(self, num):
        if len(num) >= 2:
            if num[0] > num[1]:
                return 0
            elif num[-1] > num[-2]:
                return len(num)-1
        elif len(num) == 1:
            return 0
        for i, n in enumerate(num):
            if i >= 1 and i < len(num)-1:
                if n > num[i-1] and n > num[i+1]:
                    return i

# 二分搜索/三分搜索
# 局部最小值问题

class Solution:
    def findPeakElement(self, num):
        if len(num) == 1:
            return 0
        elif num[-1] > num[-2]:
            return len(num)-1

        l, r = 0, len(num)-1
        while l <= r:
            m = (l+r) / 2
            if num[m-1] < num[m] > num[m+1]:
                return m
            elif num[m] > num[m+1]:
                r = m-1
            else:
                l = m+1
        return m

sol = Solution()
print(sol.findPeakElement([1, 2, 3, 1]))
print(sol.findPeakElement([2, 1]))
print(sol.findPeakElement([7, 8, 1, 5, 9, 6, 3, 1]))
print(sol.findPeakElement([1]))
print(sol.findPeakElement([1, 2]))
print(sol.findPeakElement([1, 2, 3]))
