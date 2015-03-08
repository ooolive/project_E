
# https://oj.leetcode.com/problems/implement-strstr/

class Solution_initial_brute_force:
    def strStr(self, heystack, needle):
        start, end = 0, len(needle)
        ltotal, lneedle = len(heystack), len(needle)
        while end <= ltotal:
            found = True
            for i in xrange(0, lneedle):
                if heystack[start+i] != needle[i]:
                    found = False
                    break
            if found:
                return start
            start += 1
            end += 1
        return -1

# 一次 AC, 貌似还是凑数的... 官方 Solution: Brute force
# 然后我这个速度还不算太差...
# 当然可以 KMP 啊, Rabin-Karp 啊, Boyer-Moore 啊
# 但是 BF 强调代码简洁性
# 而且我没有基础...

# String Match, 这是个问题...

# Still working in progress ...

# 150308 AM

s = Solution()
print(s.strStr('wenjifeiyoujichu', 'fei'))
print(s.strStr('wenjifeiyoujichu', 'chu'))
print(s.strStr('wenjifeiyoujichu', 'wen'))
print(s.strStr('wenjifeiyoujichu', 'foundation'))
