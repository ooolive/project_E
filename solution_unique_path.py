
# https://oj.leetcode.com/problems/unique-paths/

ga = [[0 for col in range(100)] for row in range(100)]
ga[0][0] = 1

def foundation_(x, y):
    if ga[x][y]:
        return ga[x][y]
    left, up = 0, 0
    if x:
        left = foundation(x-1, y)
    if y:
        up = foundation(x, y-1)
    ga[x][y] = left + up
    return left + up

def foundation(x, y):
    t = ga[x][y]
    if t:
        return t
    left, up = 0, 0
    if x:
        left = foundation(x-1, y)
    if y:
        up = foundation(x, y-1)
    ret = left + up
    ga[x][y] = ret
    return ret

class Solution:
    def uniquePaths(self, m, n):
        return foundation(m-1, n-1)

# 一次 AC 流，性能还不错，大概是因为函数中进行了一些小优化
# 避免重复计算什么的，我试图摸清 CPython 性能的脾气，但是貌似
# 基础不够很难
# tag 给的是 DP，话说 Python Core 自身竟然不大方便构造定长的
# 矩阵结构，list 搞定

# 貌似 LeetCode 支持 array 模块，没试过
# 毕竟 array 只支持几个基础数据类型 ( 是吧? )

# 150306 NOON

s = Solution()
print(s.uniquePaths(1, 1))
print(s.uniquePaths(1, 3))
print(s.uniquePaths(2, 3))
print(s.uniquePaths(3, 7))
print(s.uniquePaths(100, 100))
