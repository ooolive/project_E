
class Solution_TLE_initial:
    def maxArea(self, height):
        ret = 0
        for i in xrange(0, len(height)):
            lastlen = 0
            t = height[i]
            for j in xrange(0, i):
                if height[j] > lastlen:
                    area = min(t, height[j]) * (i - j)
                    lastlen = height[j]
                    if ret < area:
                        ret = area
        return ret

# 30% 通过率的一道题，Tag: Two Pointers
# 然后被虐了... 本来 O(n) 的整成 n^2 然后 TLE 了
# 脑子转不起来又没有基础
# 参考：https://oj.leetcode.com/discuss/22937/simple-answer-o-n
# 其实是抄...

class Solution:
    def maxArea(self, height):
        l, r, ret = 0, len(height)-1, 0
        while l < r:
            ret = max(ret, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ret

# 150304 EVE

s = Solution()
print(s.maxArea([1, 1]))
print(s.maxArea([1, 2, 3, 4, 5]))
