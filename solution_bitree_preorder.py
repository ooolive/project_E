# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def preorderTraversal(self, root):
        ret = [ ]

        t = [ ]
        t.append(root)
        while len(t):
            node_current = t.pop()
            if node_current is None:
                continue
            ret.append(node_current.val)
            t.append(node_current.right)
            t.append(node_current.left)

        return ret

# initial solution 有点慢。
s = Solution()

t = None

print(s.preorderTraversal(t))

t = TreeNode(1)

print(s.preorderTraversal(t))

t.right = TreeNode(2)

print(s.preorderTraversal(t))

t.right.left = TreeNode(3)

print(s.preorderTraversal(t))
