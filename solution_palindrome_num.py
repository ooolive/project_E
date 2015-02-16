#coding=utf-8

class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False

        length, lt = 0, 1
        while lt <= x:
            length += 1
            lt *= 10

        lo, hi = 0, length-1
        for i in range(length/2):
            a, b = x / pow(10, lo) % 10, x / pow(10, hi) % 10
            if a != b:
                return False
            lo += 1
            hi -= 1
        return True

class Solution_wtf:
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

# 这题的时间分布大概是史上见过最奇葩的...
# 而且感觉也不简单，关键是 discussion 里面
# 啥都找不到貌似，所以到最后没找到好的 Solution
# initial solution 比较一般
# 141226 EVE

s = Solution()
print(s.isPalindrome(10))
print(s.isPalindrome(123))
print(s.isPalindrome(121))
print(s.isPalindrome(123321))

