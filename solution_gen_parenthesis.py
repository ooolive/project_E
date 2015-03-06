#coding=utf-8

def foundation(n, s, t1, t2, ret):
    if t1 <= n:
        foundation(n, s+'(', t1+1, t2, ret)
    if t2 < t1:
        foundation(n, s+')', t1, t2+1, ret)
    if t1 == t2 == n:
        ret.append(s)

class Solution_initial:
    def generateParenthesis(self, n):
        ret = [ ]
        foundation(n, '', 0, 0, ret)
        return ret

# initial solution 速度还可以, 一次 AC
# tags 给的是回溯法 backtracking，老实说根本没这个的基础

class Solution:
    def generateParenthesis(self, n):
        self.ret = [ ]
        self.n = n
        self.t('', 0)
        return self.ret

    def t(self, s, t):
        if t <= self.n:
            self.t(s + '(', t+1)
        a = len(s) * 0.5
        if a < t:
            self.t(s + ')', t)
        elif a == self.n:
            self.ret.append(s)

# 试着改，并没有快到哪里去

# discuss 里面有 list comprehension
# 还有直接用 set + bruteforce
# 表示暂时并不能理解

# 150306 FRI

s = Solution()
print(s.generateParenthesis(0))
print(s.generateParenthesis(1))
print(s.generateParenthesis(2))
print(s.generateParenthesis(3))
