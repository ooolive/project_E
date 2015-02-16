#coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(root, prev):
    if root is None:
        return 0
    c = prev * 10 + root.val
    if not (root.left or root.right):
        return c
    return helper(root.left, c)+helper(root.right, c)

class Solution:
    def sumNumbers(self, root):
        return helper(root, 0)

# initial Solution 递归
# 速度只能说还可以

# 141231 NOON

s = Solution()

t = None

print(s.sumNumbers(t))

t = TreeNode(1)

print(s.sumNumbers(t))

t.left = TreeNode(2)
t.right = TreeNode(3)

print(s.sumNumbers(t))

t.left.left = TreeNode(4)

print(s.sumNumbers(t))

t.left.right = TreeNode(5)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)

print(s.sumNumbers(t))
