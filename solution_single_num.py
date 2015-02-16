class Solution:
    def singleNumber(self, A):
        ret_array = { }
        for item in A:
            ret_array[item] = not ret_array.has_key(item)
        for key, item in ret_array.iteritems():
            if item:
                return key

sol = Solution()
print(sol.singleNumber([1, 2, 3, 1, 2, 3, 4]))

# better...
# https://oj.leetcode.com/discuss/9396/challenge-me-shortest-possible-answer
def singleNumber(self, A):
        return reduce(lambda x,y:x^y,A)

# 很明显智商被爆了...
# 评论区各种秀位操作的...
