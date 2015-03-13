
# https://leetcode.com/problems/number-of-1-bits/

class Solution_initial:
    def hammingWeight(self, n):
        ret = 0

        while n:
            if n % 2:
                ret += 1
            n >>= 1

        return ret

class Solution:
    def hammingWeight(self, n):
        ret = 0
        while n:
            ret += n & 1
            n = n >> 1
        return ret

# 新出的，难度上超级简单的水题，新出的，tag 给的是 bit mani.
# 右移谁都会（虽然我最开始写成了左移吧），那个与大概有点技术含量
# 没啥 edge case 的考虑，过了基础的就行
# 现在看不到 distribution，过段时间再说
# 目测性能不会太好

# 150313 PM

s = Solution()
print(s.hammingWeight(0))
print(s.hammingWeight(1))
print(s.hammingWeight(11))
