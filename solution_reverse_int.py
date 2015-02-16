MAXINT_ORG = 2147483648
MAXINT = 214748364 # 2**31/10

class Solution_initial:
    def reverse(self, x):
        if x == 0:
            return 0
        sign = 1 if x > 0 else -1
        x /= sign
        ret = 0
        while x:
            if ret > MAXINT:
                return 0
            ret *= 10
            ret += x % 10
            x /= 10
        return ret * sign

class Solution():
    def reverse(self, x):
        sign = 1 if x > 0 else -1
        x /= sign

        s = str(x)
        ret = ''
        for c in reversed(s):
            ret += c
        ret = int(ret)
        if ret > MAXINT_ORG:
            return 0
        else:
            return ret*sign

sol = Solution()
print(sol.reverse(321))
print(sol.reverse(100))
print(sol.reverse(-321))
print(sol.reverse(1534236469))
