#encoding=utf-8

map_buttons = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
}

class Solution:
    def letterCombinations(self, src):
        prep = [ '' ]
        #prep_m = [ ]
        for c in src:
            prep = [i+j for i in prep for j in map_buttons[c]]
        #for c in src:
            #prep_m = [ ]
            #for i in prep:
                #for j in map_buttons[c]:
                    #prep_m.append(i+j)
            #prep = prep_m
        return prep

# initial solution 速度中等
# 还有 LeetCode 不能用 itertools

# 改进成 list comprehension
# 结果一点没快... 毕竟算法没变

# 141223 NOON

sol = Solution()
print(sol.letterCombinations(''))
print(sol.letterCombinations('23'))
