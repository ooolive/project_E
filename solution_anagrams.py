
# https://leetcode.com/problems/anagrams/

class Solution_initial:
    def anagrams(self, strs):
        t = { }
        ret = [ ]
        for s in strs:
            st = "".join(sorted(s))
            if st in t:
                if t[st] != False:
                    ret.append(t[st])
                    t[st] = False
                ret.append(s)
            else:
                t[st] = s

        return ret

class Solution:
    def anagrams(self, strs):
        t, ret = { }, [ ]
        for s in strs:
            st = "".join(sorted(s))
            if st in t:
                if t[st] != False:
                    ret.append(t[st])
                    t[st] = False
                ret.append(s)
            else:
                t[st] = s

        return ret

# 150314 EVE

s = Solution()

print(s.anagrams(["", ""]))
print(s.anagrams(["aabc", "bcaa", "cbaa", "aaa"]))
