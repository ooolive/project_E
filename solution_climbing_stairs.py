
# https://leetcode.com/problems/climbing-stairs/

t = [ 0 ] * 512
t[0] = t[1] = 1

def foundation(n):
    if t[n]:
        return t[n]
    t[n] = foundation(n-1) + foundation(n-2)
    return t[n]

class Solution:
    def climbStairs(self, n):
        return foundation(n)

# tag DP, һ���Ѷ�û��, discuss ��������һ������
# https://leetcode.com/discuss/27180/2ms-c-solution-o-1-space
# C++ �ĵ��� O(1) �ռ� solution
# �� py �İ� dp �������˸� decorator���Ե�
# https://leetcode.com/discuss/21197/o-log-n-integer-only-solution-in-6-lines-python-rocks
# ����˻��ĵĵ��� log(n) solution��ò�Ƹ���, ����û����ѧ����ò��Ҳ�������

# 150314 PN

s = Solution()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
