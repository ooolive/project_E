
# https://leetcode.com/problems/permutations/

def foundation(num, ret, t):
    if len(t) == len(num):
        ret.append(t)
    for n in num:
        if n not in t:
            t_ = t[:]
            t_.append(n)
            foundation(num, ret, t_)

class Solution:
    def permute(self, num):
        ret = [ ]
        foundation(num, ret, [ ])
        return ret

# ���͵ļ򵥵� backtracking���ҵ� solution ��űȽϴ�ͳ
# discuss ������������ iterative solution���뷨���ܲ���
# �����ٶ�����ȷ����py �����ܰ�...
# ���������һ�����������...
# �����������⵽�׸���ô�㣬��������ҿ��� The Alg. Design Man. ��˵...

# 150313 FRI

s = Solution()
print(s.permute([1, 2, 3]))
