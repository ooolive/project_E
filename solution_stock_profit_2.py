
class Solution_initial:
    def maxProfit(self, prices):
        if not len(prices):
            return 0
        max_profit = 0
        value_min, minidx = prices[0], 0
        value_end, endidx = prices[0], 0
        profit = 0
        for i, v in enumerate(prices):
            if v < value_min:
                value_min, minidx = v, i
            profit_t = v - value_min
            if profit_t > profit:
                profit = profit_t
                value_end, endidx = v, i
        return profit

def foundation_initial(prices, start):
    max_profit = 0
    value_min = prices[start]
    endidx = start
    for i in xrange(start, len(prices)):
        v = prices[i]
        value_min = min(value_min, v)
        if v > value_min:
            max_profit, endidx = v - value_min, i
            return max_profit + foundation(prices, endidx)
    return 0

def foundation(price, start):
    max_profit = 0
    value_min = price[0]
    for i, v in enumerate(price):
        value_min = min(value_min, v)
        if v > value_min:
            max_profit += v - value_min
            value_min = v
    return max_profit

class Solution_secondary:
    def maxProfit(self, prices):
        if not len(prices):
            return 0
        return foundation(prices, 0)

class Solution:
    def maxProfit(self, prices):
        if not len(prices):
            return 0
        max_profit, value_min = 0, prices[0]
        for i, v in enumerate(prices):
            value_min = min(value_min, v)
            if v > value_min:
                max_profit += v - value_min
                value_min = v
        return max_profit

s = Solution()

# 对 1 的算法的简单改进... tag Greedy
# 然后半睡不醒的各种手抖到处 RE，WA ...
# 本来先做的 recursive，后来一看性能不行又改 iterative
# 结果也没好到哪去

# 一看 discuss
#   ret += max(0, prices[i] - prices[i-1]);
# WTF!
# 大概理解了为啥这题通过率这么高了

# 150318 AM

print(s.maxProfit([1]))
print(s.maxProfit([]))
print(s.maxProfit([2, 1]))
print(s.maxProfit([3,2,6,5,0,3]))
print(s.maxProfit([1, 3, 4, 10]))
print(s.maxProfit([1, 3, 4, 10, 1, 3, 4, 10, 1, 3, 5, 9]))
print(s.maxProfit([2, 1, 2, 0, 1]))
print(s.maxProfit([6, 1, 3, 2, 4, 7]))
