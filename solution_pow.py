#coding=utf-8

# https://leetcode.com/problems/powx-n/

class Solution_initial:
    def pow(self, x, n):
        ret = 1
        for i in xrange(0, n):
            ret *= x
        return ret

# bruteforce initial solution
# 很慢，最后一个 case 直接 block，然后 TLE

def foundation_initial(x, n):
    if n == 1:
        return x
    if n < 0:
        x = 1 / x
        n *= -1
    ret, t = 1, n / 2
    if t >= 1:
        y = foundation(x, t)
        ret *= y * y
    if n % 2:
        ret *= x
    return ret

def foundation(x, n):
    if n < 0:
        x = 1 / x
        n *= -1
    ret, t = 1, n / 2
    if t:
        ret *= foundation(x*x, int(float(n)/2))
    return ret if not (n % 2) else ret * x

class Solution:
    def pow(self, x, n):
        return foundation(x, n)

# 分治，速度不差，但是代码貌似有点长
# 后来 LeetCode 貌似抽了，submit 不上去
# 话说 distribution 里面有 py 做到了最右边...

# discuss 里面有人用 iteration，还有人 bit operation...
# 最蛋疼的是有人用 Taylor 公式(我没基础，是这么叫吧)想要弄出 O(1) solution
# 后来的修改参考了 https://leetcode.com/discuss/20677/concise-python-solution

# 150309 MON

s = Solution()
print(s.pow(34.00515, -3)) # !!
print(s.pow(1.5, 0))
print(s.pow(1.5, 1))
print(s.pow(1.5, 2))
print(s.pow(1.5, 3))
print(s.pow(1.1, 2147483647)) # !!
