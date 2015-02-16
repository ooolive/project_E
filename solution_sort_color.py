#coding=utf-8

class Solution:
    def sortColors(self, A):
        lA = len(A)

        idx0, idx2 = None, None

        for i, v in enumerate(A):
            if v != 0:
                idx0 = i
                break
        for i, v in enumerate(reversed(A)):
            if v != 2:
                idx2 = lA - i - 1
                break
        if idx2 is None or idx0 is None:
            return

        curidx = idx0
        while curidx <= idx2:
            while A[curidx] != 1 and idx0 <= curidx <= idx2:
                if A[curidx] == 0:
                    A[curidx], A[idx0] = A[idx0], 0
                    idx0 += 1

                elif A[curidx] == 2:
                    A[curidx], A[idx2] = A[idx2], 2
                    idx2 -= 1
            curidx += 1

# initial solution 感觉好难啊...
# 各种边界条件
# 代码好乱...八成是因为今天没吃饭
# 速度不算太慢就是了
#
# 改了改也没太快..
#
# https://oj.leetcode.com/discuss/1827/anyone-with-one-pass-and-constant-space-solution
# 这小子吊炸了...

# 141215 PM

s = Solution()

t = [ 0, 1, 2, 0, 1, 2, 0, 1, 2 ]
s.sortColors(t)
print(t)

t = [ 0 ]
s.sortColors(t)
print(t)

t = [ 0, 0 ]
s.sortColors(t)
print(t)

t = [ 1, 0 ]
s.sortColors(t)
print(t)

t = [ 0, 2 ]
s.sortColors(t)
print(t)

t = [ 2, 2 ]
s.sortColors(t)
print(t)

t = [ 2, 2, 1 ]
s.sortColors(t)
print(t)

t = [0,2,1,2,0,0,1,2,1,1,1,0,2,1,2,1,1,1,1,2,1,0,0,0,1,2,2,0,2,1,0,0,1,2,2,1,2,1,0,0,0,0,2,0,2,1,2,1,1,1,1,0,1,2,0,0,0,0,0,0,2,1,1,0,0,1,1,0,0,0,0,1,1,2,2,0,2,1,1,1,2,0,1,1,1,0,2,1,1,2,2,0,1,0,0,1,0,2,2,1,2,1,2,0,0]
s.sortColors(t)
print(t)
