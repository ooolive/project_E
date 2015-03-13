#coding=utf-8

# https://oj.leetcode.com/problems/subsets/

def foundation_t(S, ret, l, t):
    c = len(t)
    if c == l:
        ret.append(t)
    if c < len(S):
        for i in S:
            if (not c or i >= t[-1]):
                a = t[:]
                a.append(i)
                foundation(S, ret, l+1, a)

def foundation(S, ret):
    for i in range(len(S)):
        t = [ ]
        for j in range(i):
            for k in range(len(S)):
                t.append(S[k])
            ret.append(t[:])

class Solution:
    def subsetsWithDup(self, S):
        ret = [ ]
        foundation(S, ret)
        return ret

s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
print(s.subsetsWithDup([]))
print(s.subsetsWithDup([0]))

