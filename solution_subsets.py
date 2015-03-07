#coding=utf-8

# https://oj.leetcode.com/problems/subsets/

def foundation(S, ret, l, t):
    c = len(t)
    if c == l:
        ret.append(t)
    if c < len(S):
        for i in S:
            if i not in t and (not c or i > t[-1]):
                a = t[:]
                a.append(i)
                foundation(S, ret, l+1, a)

class Solution:
    def subsets(self, S):
        ret = [ ]
        foundation(S, ret, 0, [])
        return ret


# backtracking again, initial solution 速度还可以
# 不过 tag 居然还给了 bit manip.
# 这货我是先看的 II, 但是感觉没啥想法...
# 不过弄完之后感觉还有点思路, 慢慢来吧

# discuss 里面有没有基础看不懂的位操作，还有迭代版
# 直接求的
# https://oj.leetcode.com/discuss/21144/65ms-python-solution-with-explanation
# 位操作的解释, 这货对长整数支持真的没有要求么?

# 150307 NOON

s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([]))
print(s.subsets([0]))

