
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_initial:
    def deleteDuplicates(self, head):
        h = head
        if h:
            c = h.next
            while c:
                if h.val == c.val:
                    h.next = c.next
                else:
                    h = c
                c = h.next
            return head

class Solution:
    def deleteDuplicates(self, head):
        h = head
        while h:
            while h.next and h.val == h.next.val:
                h.next = h.next.next
            h = h.next
        return head

# 两个 solution，第二个从网上抄来的，除了变量名之外一模一样
# 然后性能都差不多 (差)，复杂度一样
# nmb 的 py 的性能是怎么回事
# 这几个 list 的 utility 该改成库了啊...

# 150311 AM

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

t = create_list([1, 1, 2, 3, 3])
print_list(t)
s.deleteDuplicates(t)
print_list(t)
print()

t2 = create_list([1, 1, 2])
print_list(t2)
s.deleteDuplicates(t2)
print_list(t2)
print()

t3 = create_list([1, 1])
print_list(t3)
s.deleteDuplicates(t3)
print_list(t3)
print()

t4 = create_list([1])
print_list(t4)
s.deleteDuplicates(t4)
print_list(t4)
print()

s.deleteDuplicates([ ])

