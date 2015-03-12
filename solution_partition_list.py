
# https://leetcode.com/problems/partition-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_initial:
    def partition(self, head, x):
        fake_head = ListNode(0)
        fake_head.next = head
        p = pt = fake_head

        while p.next:
            if p.next.val < x:
                if p != pt:
                    n = p.next
                    p.next, n.next, pt.next = n.next, pt.next, p.next
                    p = n.next
                    pt = pt.next
                    continue
                pt = pt.next
            p = p.next
        return fake_head.next

class Solution:
    def partition(self, head, x):
        small_head, large_head = ListNode(0), ListNode(0)
        sh, lh, p = small_head, large_head, head
        while p:
            if p.val < x:
                sh.next = sh = p
            else:
                lh.next = lh = p
            p = p.next
        lh.next, sh.next = None, large_head.next
        return small_head.next

# 不难，但是也憋了半天...
# 各种 edge case，整到最后也没见性能有多好
# 两个 solution，不知道第二个有没有用，但是我感觉
# 第二个干净多了
# discuss 里面没几个 py 的，懒得看了

# 150312 PM

s = Solution()

def create_list(l):
    if len(l):
        head = ListNode(l[0])
        prev = head
        for i, v in enumerate(l):
            if i:
                t = ListNode(v)
                prev.next = t
                prev = t
        return head

def print_list(head):
    while head:
        print (head.val)
        head = head.next

def print_val(node):
    if node.next:
        print(node.val, ' -> ', node.next.val)
    else:
        print(node.val, ' -> ', 'null')

t = create_list([1, 4, 3, 2, 5, 2])
print_list(t)
t_ = s.partition(t, 3)
print_list(t_)
print_val(t_)
print_val(t_.next)
print_val(t_.next.next)
print_val(t_.next.next.next)
print_val(t_.next.next.next.next)
print_val(t_.next.next.next.next.next)

print()

t2 = create_list([1, 1, 1, 1, 1, 1])
print_list(t2)
print_list(s.partition(t2, 2))

print_list(s.partition(None, 3))
print_list(s.partition(ListNode(0), 3))
print_list(s.partition(ListNode(4), 3))

t3 = create_list([3, 1, 2])
print_list(t3)
print_list(s.partition(t3, 3))
