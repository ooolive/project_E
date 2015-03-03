
class Solution:
    def generate(self, numRows):
        ret = [ ]
        for i in range(0, numRows):
            t = [ 1 ]
            for j in range(1, i):
                t.append(ret[-1][j-1]+ret[-1][j])
            t.append(1)
            ret.append(t)
        if len(ret):
            ret[0] = [ 1 ]
        return ret

# another solution in discussion, more concise

class Solution_Alt:
    # return a list of lists of integers
    def generate(self, numRows):
        if not numRows: return []
        out = [[1 for i in xrange(row)] for row in xrange(1, numRows+1)]
        for row in xrange(1, numRows):
            for i in xrange(1, row): out[row][i] = out[row-1][i-1] + out[row-1][i]
        return out

s = Solution()
print(s.generate(0))
print(s.generate(1))
print(s.generate(2))
print(s.generate(5))

# 150303 TUE
