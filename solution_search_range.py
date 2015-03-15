
# https://leetcode.com/problems/search-for-a-range/

def find_a_num(A, target):
    l, r = 0, len(target)-1
    while r >= l:
        mid = (l+r) / 2

        if target[mid] < A:
            l = mid+1
        elif target[mid] > A:
            r = mid-1
        else:
            return mid
    return -1

def find_for_border(A, target, l, r, isL):
    while 1:
        mid = (l+r)/2
        if isL:
            if target[mid] != A:
                if mid == l:
                    return r
                l = mid
            else:
                r = mid
        else:
            if target[mid] != A:
                r = mid
            else:
                if mid == l:
                    return l
                l = mid

class Solution:
    def searchRange(self, target, A):
        anum_pos = find_a_num(A, target)
        if anum_pos == -1:
            return [-1, -1]
        if target[0] == A:
            lpos = 0
        else:
            lpos = find_for_border(A, target, 0, anum_pos, True)
        if target[-1] == A:
            rpos = len(target)-1
        else:
            rpos = find_for_border(A, target, anum_pos, len(target)-1, False)
        return [lpos, rpos]

# 好特么麻烦的一道题...
# 貌似没有特别好的算法，我也没搞出特别好的性能
# 一堆 edge case，论没基础刷题的艰难...
# discuss 里面有更 concise 的，有用 mid 标识结果段中间二分的
# 有用 +/- 0.5 的 trick 做的
# 我实在懒得再改了，吃点东西看一点 ML 睡觉了

# 150315 EVE

s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
print(s.searchRange([1], 0))
print(s.searchRange([1], 1))
print(s.searchRange([2, 2], 2))
print(s.searchRange([1, 2, 2], 2))
