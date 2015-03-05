#coding=utf-8

# https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None

class Solution_initial:
    def flatten(self, root):
        def t(root):
            #print("calling", root.val)
            if root.left or root.right:
                ret, ret_ = None, None
                if root.left:
                    ret = t(root.left)
                if root.right:
                    ret_ = t(root.right)
                if root.left:
                    if root.right:
                        ret.right = root.right
                    root.right = root.left
                    root.left = None
                if ret_:
                    #print("returning", ret_.val)
                    return ret_
                else:
                    #print("returning", ret.val)
                    return ret
            else:
                return root
        if root:
            t(root)

# initial solution, OS 课程上面脑补出来的
# 题不算难，但是有点乱搞得效率很低...

def f_helper(root):
    a, b = root, None
    if root.right:
        b = f_helper(root.right)
    if root.left:
        a = f_helper(root.left)
        a.right = root.right
        root.right = root.left
        root.left = None
    return (b or a)

class Solution:
    def flatten(self, root):
        if root:
            f_helper(root)

# 第二个好多了
# Solution 里面有不同的方法，恩还有迭代的...

# 150305 PM

def ptest(root):
    while root:
        print(root.val)
        root = root.right

s = Solution()

t = TreeNode(1)
t.left, t.right = TreeNode(2), TreeNode(5)
t.left.left, t.left.right = TreeNode(3), TreeNode(4)
t.right.right = TreeNode(6)

u = TreeNode(1)
u.left, u.right = TreeNode(2), TreeNode(7)
u.left.left, u.left.right = TreeNode(3), TreeNode(6)
u.left.left.left, u.left.left.right = TreeNode(4), TreeNode(5)
u.right.left, u.right.right = TreeNode(8), TreeNode(9)

v = TreeNode(1)
v.left = TreeNode(2)
v.left.left = TreeNode(3)

s.flatten(t)
ptest(t)

s.flatten(u)
ptest(u)

s.flatten(v)
ptest(v)

s.flatten(None)
ptest(None)
