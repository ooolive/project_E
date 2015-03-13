
# https://leetcode.com/problems/number-of-1-bits/

class Solution_initial:
    def hammingWeight(self, n):
        ret = 0

        while n:
            if n % 2:
                ret += 1
            n >>= 1

        return ret

class Solution:
    def hammingWeight(self, n):
        ret = 0
        while n:
            ret += n & 1
            n = n >> 1
        return ret

# �³��ģ��Ѷ��ϳ����򵥵�ˮ�⣬�³��ģ�tag ������ bit mani.
# ����˭���ᣨ��Ȼ���ʼд�������ưɣ����Ǹ������е㼼������
# ûɶ edge case �Ŀ��ǣ����˻����ľ���
# ���ڿ����� distribution������ʱ����˵
# Ŀ�����ܲ���̫��

# 150313 PM

s = Solution()
print(s.hammingWeight(0))
print(s.hammingWeight(1))
print(s.hammingWeight(11))
