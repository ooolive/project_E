#coding=utf-8

# https://leetcode.com/problems/jump-game/

class Solution_initial:
    def canJump(self, A):
        i = 0
        while i < len(A):
            maxdis = A[i]
            far, d = 0, i
            for dis in range(maxdis+1):
                if i+dis < len(A):
                    t = i + dis + A[i+dis]
                    if t > far:
                        far = t
                        d = i+dis
                else:
                    return True
            if far >= len(A)-1:
                return True
            if i == d:
                return False
            i = d
        return False

class Solution_second:
    def canJump(self, A):
        i, l = 0, len(A)
        while i < l-1:
            m = A[i]
            if not m:
                return False
            if i + m + 1 >= l:
                return True
            d = i+m
            far = d+A[d]
            for dis in xrange(m):
                a = i+dis
                t = a + A[a]
                if t > far:
                    far, d = t, a
            i = d
        return True

class Solution:
    def canJump(self, A):
        j, l = 1, len(A)-1
        for i in xrange(l):
            j -= 1
            j = max(j, A[i])
            if j == 0:
                return False
        return True

# initial solution 慢的一笔
# 后来改了半天，速度还凑合
# 但是代码太啰嗦，算法太复杂
# 后来一看 discuss 各种 concise

# 这题有点 ACM 的感觉
# 都是因为没有基础
# tag: greedy

# 150310 EVE

s = Solution()
print(s.canJump([]))
print(s.canJump([0]))
print(s.canJump([1]))
print(s.canJump([2, 3, 1, 1, 4]))
print(s.canJump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))
print(s.canJump([3, 2, 1, 0, 4]))
print(s.canJump([5, 0, 4, 6, 0, 8, 8, 4, 5, 4, 0, 6, 3, 5, 1, 2, 9, 9, 3, 0, 2, 4, 7, 5, 7, 3, 6, 5, 5, 9, 1, 3, 6, 1, 2, 3, 4, 3, 3, 1, 8, 8, 0, 7, 6, 4, 0, 0, 5, 3, 9, 3, 6, 9, 7, 4, 1, 3, 3, 5, 3, 4, 2, 6, 3, 4, 6, 8, 8, 8, 8, 8, 3, 8, 5, 0, 3, 9, 6, 3, 7, 0, 1, 4, 5, 0, 9, 8, 0, 5, 8, 0, 8, 7, 8, 8, 4, 1, 1, 9]))
