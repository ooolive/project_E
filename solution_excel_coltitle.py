#coding=utf-8

CONV_MAP = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', xrange(0, 26)))

class Solution:
    def titleToNumber(self, s):
        ret = 0
        for ch in s:
            ret *= 26
            ret += ord(ch)-64
        return ret

# 今天早上（下午两点半）的早（下午）安水题
# 算是最近几天最水的之一，新的 Easy 题还看不出 runtime dist
#
# 141229 PM

# reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))
# https://oj.leetcode.com/discuss/19675/one-line-python-code-using-map-reduce
# 恩这哥们直接 mapreduce... 吊

s = Solution()
print(s.titleToNumber(''))
print(s.titleToNumber('A'))
print(s.titleToNumber('Z'))
print(s.titleToNumber('AA'))
print(s.titleToNumber('AB'))
