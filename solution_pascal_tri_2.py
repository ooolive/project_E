
class Solution:
    def getRow(self, rowIndex):
        ret, t = [ 1 ] * (rowIndex + 1), [ 1 ] * (rowIndex + 1)
        for i in xrange(0, rowIndex/2+1):
            ret[i] = t[rowIndex-i]
            for j in xrange(1, rowIndex-i):
                t[j] += t[j-1]
        for i in xrange(0, rowIndex / 2+1):
            ret[rowIndex-i] = ret[i]
        return ret

class Solution_magic:
    def getRow(self, rowIndex):
        return reduce(lambda lst,i: lst + [lst[-1]*(rowIndex-i+1)/i], [[1]] + range(1,rowIndex+1))

# Easy 题, 然后拿纸笔画了半天还弄出个 n^2 Solution...
# 数学基础不好的后果...
# discuss 里面有超吊的 O(n) solution

# WIP.

# 150308 EVE

s = Solution()
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(2))
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))
