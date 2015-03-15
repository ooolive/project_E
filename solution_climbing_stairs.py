
# https://leetcode.com/problems/climbing-stairs/

t = [ 0 ] * 512
t[0] = t[1] = 1

def foundation(n):
    if t[n]:
        return t[n]
    t[n] = foundation(n-1) + foundation(n-2)
    return t[n]

class Solution:
    def climbStairs(self, n):
        return foundation(n)

# tag DP, 一点难度没有, discuss 里面照样一堆奇葩
# https://leetcode.com/discuss/27180/2ms-c-solution-o-1-space
# C++ 的迭代 O(1) 空间 solution
# 有 py 的把 dp 部分做了个 decorator，略吊
# https://leetcode.com/discuss/21197/o-log-n-integer-only-solution-in-6-lines-python-rocks
# 矩阵乘积的的迭代 log(n) solution，貌似更叼, 但是没有数学基础貌似也很难理解

# 150314 PN

s = Solution()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
