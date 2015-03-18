
# https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix):
        lx, ly = len(matrix[0]), len(matrix)
        next_zeroed = first_zero = False
        for x in range(lx):
            if matrix[0][x] == 0:
                next_zeroed = first_zero = True
                break
        for x in range(lx):
            for ya in xrange(ly):
                if matrix[ya][x] == 0:
                    matrix[0][x] = 0
        for y in range(1, ly):
            t = False
            for x in range(lx):
                if matrix[y][x] == 0:
                    t = True
                if matrix[y-1][x] == 0:
                    matrix[y][x] = 0
                else:
                    if matrix[0][x] == 0:
                        matrix[y][x] = 0
            if next_zeroed and y != 1:
                for x in range(lx):
                    matrix[y-1][x] = 0
            next_zeroed = t
        if next_zeroed:
            for x in range(lx):
                matrix[-1][x] = 0
        if first_zero:
            for x in range(lx):
                matrix[0][x] = 0

# 整了一个小时的一个玩意...
# 变态之处在于要求 O(1) space，完后想了半天
# 整出一个还凑合的 solution，结果是爆了 distribution 的表...
# 简直汗如雨下... 而且一点也不简洁
# 优化之后更蛋疼了...
# discuss 里面大部分比较正常的 solution 也不短
# 不过起码比你这玩意好多了啊
# 用第一行做缓存，跳一行清空行

# 150318 EVE

from pprint import pprint

s = Solution()

t = [[1, 1, 0, 4, 5], [6, 7, 5, 9, 9], [1, 2, 4, 4 ,5], [6, 7, 4, 9, 5]]
pprint(t)
s.setZeroes(t)
pprint(t)

s.setZeroes([[ 0 ]])

t = [[1], [0]]
s.setZeroes(t)
pprint(t)
