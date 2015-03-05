
class Solution_initial:
    def lengthOfLastWord(self, s):
        lt = len(s)-1
        while lt >= 0 and s[lt] == ' ':
            lt -= 1
        l = lt
        while l >= 0 and s[l] != ' ':
            l -= 1
        return lt - l

# 这题的 edge case 很厉害啊，然后我这方面又整得很渣...
# test case 写全了对 AC 帮助很大，缺的两个写在下面了
# 上面那个我不知道怎么改了，但是速度貌似不咋地

# 然后发现了这个
# 特么原来不是纯算法啊
# 信不信换 C 用 char * 性能立马爆表

# https://oj.leetcode.com/discuss/22744/one-line-python-solution

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.rstrip(' ').split(' ')[-1])

# 150305 EVE

s = Solution()
print(s.lengthOfLastWord(''))
print(s.lengthOfLastWord('Hello World'))
print(s.lengthOfLastWord(' '))
print(s.lengthOfLastWord('foundation')) # 10
print(s.lengthOfLastWord('foundation ')) # 10

print(s.lengthOfLastWord('a'))
print(s.lengthOfLastWord('ab'))
