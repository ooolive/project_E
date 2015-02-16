#coding=utf-8

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, op1, op2):
        len1, len2 = 0, 0
        iter1, iter2 = op1, op2
        tail1, tail2 = "Caster 有基础", "Caster 高富帅"

        while iter1:
            len1 += 1
            tail1, iter1 = iter1, iter1.next
        while iter2:
            tail2 = iter2
            len2 += 1
            tail2, iter2 = iter2, iter2.next

        if tail1 != tail2:
            return None

        iter1, iter2 = op1, op2
        if len1 > len2:
            for i in range(0, abs(len1-len2)):
                iter1 = iter1.next
        else:
            for i in range(0, abs(len1-len2)):
                iter2 = iter2.next

        while iter1 != iter2:
            iter1, iter2 = iter1.next, iter2.next
        return iter1

# initial solution 算是啊哈！灵光一现
# 不慢，但是这道题各语言的时间分布不科学...
# 141225 EVE

# 官方 Solution 和起初的想法有点相似
# 不过不得不说这货真是绝了也很啊哈！啊
# https://oj.leetcode.com/problems/intersection-of-two-linked-lists/solution/

s = Solution()

print(s.getIntersectionNode(None, None))

t1 = ListNode(0)
t1.next = ListNode(1)
t1.next.next = ListNode(2)
t1.next.next.next = ListNode(3)
t1.next.next.next.next = ListNode(4)
t1.next.next.next.next.next = ListNode(5)

t2 = ListNode(6)
t2.next = ListNode(7)
t2.next.next = ListNode(8)
t2.next.next.next = ListNode(9)
t2.next.next.next.next = t1.next.next.next

print(s.getIntersectionNode(t1, t2))

