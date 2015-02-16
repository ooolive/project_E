class Solution_dict:
    def majorityElement(self, num):
        td = { }
        for n in num:
            if td.has_key(n):
                td[n] += 1
            else:
                td[n] = 1
        for n, t in td.iteritems():
            if t > len(num)/2:
                return n


# Moore's voting algorithm
# https://oj.leetcode.com/discuss/19153/solution-using-moores-voting-algorithm-runtime-comlexity

class Solution:
    def majorityElement(self, num):
        idx, cnt, cur_n = 0, 0, num[0]
        for i, n in enumerate(num):
            cnt += 1 if (n == cur_n) else -1
            if cnt < 0:
                cnt = 1
                idx = i
                cur_n = n
        return cur_n

sol = Solution()
print(sol.majorityElement([1, 2, 4, 4, 4, 4, 4, 5]))

# 嗯随机算法...
# 位操作依然神器
