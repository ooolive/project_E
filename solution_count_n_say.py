
# https://leetcode.com/problems/count-and-say/

store = [ None ] * 1024

def foundation_initial(last, n, t):
    if not n:
        return last
    if store[t-n+1]:
        return foundation(store[t-n], n-1, t)
    i, new, l = 0, '', len(last)
    while i < l:
        cur, j = last[i], i
        while j < l and last[j] == cur:
            j += 1
        new += str(j-i) + cur
        i = j
    store[t-n] = new
    return foundation(new, n-1, t)

class Solution:
    def countAndSay(self, n):
        last = '1'
        while n > 1:
            i, new, l = 0, '', len(last)
            while i < l:
                cur, j = last[i], i
                while j < l and last[j] == cur:
                    j += 1
                new += str(j-i) + cur
                i = j
            n -= 1
            last = new
        return last
        #return foundation('1', n-1)

# 这东西是不是没有更好的算法啊...
# Python 的倒真是花样多，递归的，迭代的，itertools.groupby 的
# itertools.takewhile 的, string.format 的, 甚至 regexp 的...
# 最后没搞出太好的性能, 没 profile 不知道瓶颈在哪
# DP 不知道有没有用，但是我也不知道 Judge 那边的测试方式啊...

# 150309 MON

s = Solution()
print(s.countAndSay(1))
print(s.countAndSay(2))
print(s.countAndSay(3))
print(s.countAndSay(4))
print(s.countAndSay(5))
print(s.countAndSay(6))

print()

for i in range(1, 20):
    print(i, s.countAndSay(i), len(s.countAndSay(i)))
