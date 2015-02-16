#coding=utf-8

class Solution_initial:
    def findMin(self, num):
        p = num[0]
        for i in num:
            if i < p:
                return i
            p = i
        return num[0]

# 这货的 edge case 貌似有点烦人
# 不过没有空输入
# WA 了若干次，应该不是正统答案
#
# Solution 里面给出的
# 可以用类二分方法，O(logn)
#
# 141230 PM

class Solution:
    def findMin(self, num):
        sl, sr, al, ar = 0, len(num)-1, num[0], num[-1]
        if ar > al:
            return al
        while sl != sr:
            sm = (sl+sr)/2
            if num[sm] < ar:
                sr = sm
            else:
                sl = sm+1
        return num[sl]

# 第二个 Solution 搞得这个纠结...
# 不过性能貌似没太大突破

s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
print(s.findMin([1]))
print(s.findMin([1, 2]))
print(s.findMin([2, 1]))
print(s.findMin([3, 1, 2]))

