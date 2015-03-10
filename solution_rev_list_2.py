
# https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        p = head
        for i in range(m-2):
            p = p.next

        if m > 1:
            subl_headprev = p
            p = p.next
        subhead = prevh = f = p
        p = p.next
        for i in range(m, n):
            f, p.next = p.next, prevh
            prevh, p = p, f

        subhead.next = f
        if m > 1:
            subl_headprev.next = prevh
            return head
        else:
            return prevh

# ranged, in-place, one-pass, edge-cases
# 大概不可能 Pythonic...
# discuss 里面也没找到什么好的 py solution
# 算法参照 CII 里面的一个小链表倒置例程
# 卡了一中午，性能没见多好

# 150310 NOON

s = Solution()

tl = [ListNode(i) for i in range(1, 6)]
for i, v in enumerate(tl[:-1]):
    v.next = tl[i+1]

t = tl[0]

def print_list(head):
    while head:
        print (head.val)
        head = head.next

def print_val(node):
    if node.next:
        print(node.val, ' -> ', node.next.val)
    else:
        print(node.val, ' -> ', 'null')

for v in tl:
    print_val(v)

print_list(t)
s.reverseBetween(t, 3, 5)
print_list(t)

for v in tl:
    print_val(v)

t2 = ListNode(3)
t2_2 = ListNode(5)
t2.next = t2_2
print_list(t2)
print_list(s.reverseBetween(t2, 1, 2))
print_list(t2_2)
