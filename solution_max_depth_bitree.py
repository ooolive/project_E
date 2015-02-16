#coding=utf-8

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution_rec:
    def maxDepth(self, root):
        if root == None:
            return 0
        a = self.maxDepth(root.left)
        b = self.maxDepth(root.right)
        if a > b:
            return a+1
        else:
            return b+1

class Solution_stack:
    def maxDepth(self, root):
        if root is None:
            return 0
        st = [ ]
        st_depth = [ ]
        st.append(root)
        st_depth.append(1)
        max_dp = 0
        while len(st):
            node = st.pop()
            node_dp = st_depth.pop()

            node_l, node_r = node.left, node.right
            if node_l:
                st.append(node_l)
                st_depth.append(node_dp+1)
            if node_r:
                st.append(node_r)
                st_depth.append(node_dp+1)

            if node_dp > max_dp:
                max_dp = node_dp

        return max_dp

# Python 的递归...
# 真 TM 快

# simpler, *Pythonic*
# not the fastest

# https://oj.leetcode.com/discuss/13787/accepted-answer-but-had-to-externalize-the-method
def depth(root):
    if root is None:
        return 0
    return max(depth(root.left), depth(root.right))+1

class Solution:
    def maxDepth(self, root):
        return depth(root)

sol = Solution()

print(sol.maxDepth(None))

t1 = TreeNode(1)

print(sol.maxDepth(t1))

t1.left = TreeNode(1)

print(sol.maxDepth(t1))

t1.right = TreeNode(1)

print(sol.maxDepth(t1))

t1.right.right = TreeNode(1)

print(sol.maxDepth(t1))
