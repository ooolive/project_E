
# https://leetcode.com/problems/two-sum/

class Solution_initial:
    def twoSum(self, num, target):
        t = { }
        for i, n in enumerate(num):
            t[n] = i+1
        for i, n in enumerate(num):
            if (target-n) in t and t[target-n] != i+1:
                return sorted((i+1, t[target-n]))

class Solution:
    def twoSum(self, num, target):
        t = { }
        for i, n in enumerate(num):
            t[n] = i
        for i, n in enumerate(num):
            a = target - n
            if a in t:
                b = t[a]
                if i < b:
                    return (i+1, b+1)
                elif i > b:
                    return (b+1, i+1)

# LC 的第一道题，tag 给的蛤希
# 各种 edge case... AC 率有点低
# 性能不算太差
# 凑合过了，discuss 里面有非蛤希的 solution

# 150311 NOON

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([-1, -2, -3, -4, -5], -8)) # !
print(s.twoSum([3, 2, 4], 6)) # !
print(s.twoSum([0, 4, 3, 0], 0)) # !
