
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def move_backward_initial(A, start, distance, end):
    #print(A, start, distance, end)
    for i in xrange(start, end):
        A[i-distance] = A[i]


class Solution_initial:
    def removeDuplicates(self, A):
        l = len(A)
        l_ret = 0
        i = 0
        while i < l-1:
            probe = i
            while probe < l-1 and A[i] == A[probe]:
                probe += 1
            t = A[probe]
            for j in range(i+1, probe):
                A[j] = t
            i += 1
        prev = False
        for v in A:
            if v == prev:
                break
            else:
                prev = v
                l_ret += 1
        return l_ret

class Solution:
    def removeDuplicates(self, A):
        if not len(A):
            return 0
        i = p = 0
        for i in xrange(len(A)-1):
            if A[i+1] != A[i]:
                p += 1
                A[p] = A[i+1]
        return p+1

# 你知道什么叫卧槽么。
# initial TLE，TLE，还有 TLE。
# 完后十行代码解决
# 关键是这十行代码不是我自己想出来的

# 150319 NOON

s = Solution()

t = [ ]
print(s.removeDuplicates(t))

t = [1, 1, 2]
print(s.removeDuplicates(t))
print(t)

t = [1, 2, 3, 4, 4, 4, 5, 6, 7]
print(s.removeDuplicates(t))
print(t)

t = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
print(s.removeDuplicates(t))
print(t)
