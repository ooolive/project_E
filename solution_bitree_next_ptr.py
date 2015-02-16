#coding=utf-8

# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None

def helper(root):
    if root.left:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        helper(root.left)
        helper(root.right)

class Solution_initial:
    def connect(self, root):
        if root:
            helper(root)

# 这个 Solution 很简单，速度不慢
# 但是想了半天
# 最重要的是违反了题目一条规矩，使用了栈空间
# 显然太 naive

class Solution:
    def connect(self, root):
        if root and root.left:
            root.left.next = root.right
            l_master = root.left
            while l_master.left:
                cur = l_master
                while cur.next:
                    cur.left.next = cur.right
                    cur.right.next = cur.next.left
                    cur = cur.next
                cur.left.next = cur.right
                l_master = l_master.left

# 第二个空间 O(1) 的 Solution，一轮 AC 而且还很快
# —— 的感觉好爽啊...
# 不过显然不如上面的 Pythonic σ(o´з｀o)
# "感谢选择百度/阿里/中科院，再见。"
#   GvR: "怪我咯 m(￣ｰ￣)m"
#   
# 141224 EVE

s = Solution()

n = None

#print(s.connect(n))

n = TreeNode(0)

#print(s.connect(n))

n.left = TreeNode(1)
n.right = TreeNode(2)
n.left.left = TreeNode(3)
n.left.right = TreeNode(4)
n.right.left = TreeNode(5)
n.right.right = TreeNode(6)


n.left.left.left = TreeNode(7)
n.left.left.right = TreeNode(8)
n.left.right.left = TreeNode(9)
n.left.right.right = TreeNode(10)
n.right.left.left = TreeNode(11)
n.right.left.right = TreeNode(12)
n.right.right.left = TreeNode(13)
n.right.right.right = TreeNode(14)

print(s.connect(n))

print(n.next, n.left.next, n.right.next)
print(n.left.left.next, n.left.right.next, n.right.left.next, n.right.right.next)
print(n.left.right.right.next)
