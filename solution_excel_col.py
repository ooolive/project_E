BASE = 26
CONV_MAP = dict(zip(xrange(0, 26), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

class Solution:
    def convertToTitle(self, num):
        ret = [ ]
        while num > 0:
            cur_n = (num-1) % BASE
            ret.append(cur_n)
            num = (num-1) / BASE

        return ''.join([CONV_MAP[item] for item in reversed(ret)])

sol = Solution()
print(sol.convertToTitle(1))
print(sol.convertToTitle(2))
print(sol.convertToTitle(26))
print(sol.convertToTitle(27))
print(sol.convertToTitle(28))
print(sol.convertToTitle(52))
print(sol.convertToTitle(56))
print(sol.convertToTitle(255))
print(sol.convertToTitle(700))
print(sol.convertToTitle(701))
