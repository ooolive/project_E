
# https://leetcode.com/problems/combination-sum/

def foundation_initial(candidates, target, cur, curs, ret):
    if curs == target:
        ret.append(cur)
        return
    else:
        if target - curs >= candidates[0]:
            for candidate in candidates:
                if len(cur) and cur[-1] <= candidate:
                    t = cur[:]
                    t.append(candidate)
                    foundation(candidates, target, t, curs+candidate, ret)
                elif not len(cur):
                    t = cur[:]
                    t.append(candidate)
                    foundation(candidates, target, t, candidate, ret)

class Solution_initial:
    def combinationSum(self, candidates, target):
        if not len(candidates):
            return [ ]
        ret = [ ]
        s = sorted(candidates)
        foundation(s, target, [ ], 0, ret)
        return ret

def foundation(candidates, target, cur, curs, ret):
    if target - curs >= candidates[0]:
        for candidate in candidates:
            if cur[-1] <= candidate:
                t = cur[:]
                t.append(candidate)
                result = curs + candidate
                if result == target:
                    ret.append(t)
                    continue
                elif result > target:
                    continue
                else:
                    foundation(candidates, target, t, result, ret)

class Solution:
    def combinationSum(self, candidates, target):
        ret = [ ]

        if len(candidates):

            m, idx = candidates[0], 0
            for i, v in enumerate(candidates):
                if v < m:
                    m, idx = v, i
            candidates[0], candidates[idx] = candidates[idx], candidates[0]

            for candidate in candidates:
                if candidate < target:
                    foundation(candidates, target, [ candidate ], candidate, ret)
                elif candidate == target:
                    ret.append([ candidate ])

        return ret

# tag Backtracking, 挺简单的, 最近写的有点多...
# 我的大概还是最传统的方法，然后啰嗦的一笔...
# discuss 里面见到的最创新的大概是这个
# https://leetcode.com/discuss/21545/accepted-recursive-solution-in-python

# 150316 EVE

s = Solution()
print(s.combinationSum([], 7))
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([8, 7, 4, 3], 11))
