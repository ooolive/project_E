
# https://leetcode.com/problems/permutations/

def foundation(num, ret, t):
    if len(t) == len(num):
        ret.append(t)
    for n in num:
        if n not in t:
            t_ = t[:]
            t_.append(n)
            foundation(num, ret, t_)

class Solution:
    def permute(self, num):
        ret = [ ]
        foundation(num, ret, [ ])
        return ret

# 典型的简单的 backtracking，我的 solution 大概比较传统
# discuss 里面有若干种 iterative solution，想法都很不错
# 不过速度难以确定，py 的性能啊...
# 最吊的是有一个用随机采样...
# 至于这种问题到底该怎么搞，过半年等我啃完 The Alg. Design Man. 再说...

# 150313 FRI

s = Solution()
print(s.permute([1, 2, 3]))
