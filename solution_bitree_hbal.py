#coding=utf-8

# defintion for a binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def depth_max(root):
    if root is None:
        return 0
    return max(depth_max(root.left)+1, depth_max(root.right)+1)

def depth_min(root):
    if root is None:
        return 0
    return min(depth_min(root.left)+1, depth_min(root.right)+1)

def bal_helper(root):
    if root is None:
        return True, 0
    bal_l, dpl = bal_helper(root.left)
    bal_r, dpr = bal_helper(root.right)
    if (bal_l and bal_r) == False:
        return False, 0
    if abs(dpl - dpr) <= 1:
        return True, max(dpl, dpr)+1
    else:
        return False, 0

class Solution_initial:
    def isBalanced(self, root):
        return bal_helper(root)[0]

# 特么表面看着不难
# 完后发现根本没办法搞...
# initial solution 不算太慢
# 但是 WA 了好几次
# 注意题目定义是 a height-balanced binary tree is defined as a binary
# tree in which the depth of the two subtrees of every node never differ by more than 1.

WA = -19961208

def depth_hp(root):
    if root is None:
        return 0
    dpl, dpr = depth_hp(root.left), depth_hp(root.right)
    if dpl == WA or dpr == WA or abs(dpl-dpr) > 1:
        return WA
    return max(dpl, dpr)+1

class Solution:
    def isBalanced(self, root):
        return depth_hp(root) != WA

# Solution 2 借鉴了 https://oj.leetcode.com/discuss/12331/accepted-o-n-solution
# 丧心病狂的把 balanced 整合到了 depth 里面
# 结果返回元组变成了返回单个值，貌似快了不少
# 不过把 helper 函数局部化之后虽然干净，但是会出现 recursion limit 的问题
# discussion 里面貌似也有人提到了，但是全局的 helper 是 AC 的
# 难道这 Python 的处理有区别？

sol = Solution()

print(sol.isBalanced(None))

t1 = TreeNode(1)

print(sol.isBalanced(t1))

t1.left = TreeNode(1)

print(sol.isBalanced(t1))

t1.right = TreeNode(1)

print(sol.isBalanced(t1))

t1.right.right = TreeNode(1)

print(sol.isBalanced(t1))

t1.right.right.right = TreeNode(1)

print(sol.isBalanced(t1))

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.left.left = TreeNode(3)
t2.left.left.left = TreeNode(4)
t2.right = TreeNode(2)
t2.right.right = TreeNode(3)
t2.right.right.right = TreeNode(4)

print(sol.isBalanced(t2))
