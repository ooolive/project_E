#coding=utf-8

class Solution_initial:
    def maxProfit(self, prices):
        if len(prices) <= 0:
            return 0
        max_array = [ prices[-1] ]
        for i in xrange(0, len(prices)-1):
            max_array.append(max(max_array[i], prices[-i-1]))
        return max(max_array[-i-1]-prices[i] for i in xrange(0, len(prices)))

        #for i, v in enumerate(reversed(prices)):
            #if i > 0:
                #if v > max_array[i-1]:
                    #max_array.append(v)
                #else:
                    #max_array.append(max_array[i-1])

        #max_profit = 0
        #for i, v in enumerate(prices):
            #profit = max_array[-i-1]-v
            #if profit > max_profit:
                #max_profit = profit

        #return max_profit

# initial solution 一次 AC
# 速度中等

# 话说今天真是有够懒，下午才爬起来做...
# 后来简化了代码，性能貌似没提升

class Solution:
    def maxProfit(self, prices):
        if len(prices) <= 0:
            return 0
        profit, min_price = 0, prices[0]
        for v in prices:
            min_price = min(min_price, v)
            profit = max(profit, v-min_price)
        return profit

# 这个大概是最叼的 Solution...
# O(n) 时间 O(1) 空间，1 pass
# https://oj.leetcode.com/discuss/2565/is-something-wrong-with-the-test-case
#
# 141226 PM

s = Solution()
print(s.maxProfit([1]))
print(s.maxProfit([]))
print(s.maxProfit([3,2,6,5,0,3]))
print(s.maxProfit([1, 3, 4, 10]))
