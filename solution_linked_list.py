#coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        t = ListNode(0)
        while 1:
            if head == None:
                return False
            elif head is t:
                return True
            head.next, head = t, head.next

# initial solution, 感觉简直绝了...
# 被基础坑回来的路上想出来的招
# 很快，但是 trivial
# 还有 Python 的元组解包是有赋值顺序的？

class Solution_discussion:
    def hasCycle(self, head):
        slow = fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# 咳咳正餐来了，Floyd's Cycle-Finding Algorithm
# 大概是最正统的算法，恩我当时想的是两个指针
# 差一步同步走...

# 141228 EVE

s = Solution()

t = None

print(s.hasCycle(t))

t = ListNode(1)

print(s.hasCycle(t))

t.next = ListNode(2)

print(s.hasCycle(t))

t.next.next = ListNode(3)

t.next.next.next = ListNode(4)

t.next.next.next.next = t.next

print(s.hasCycle(t))
