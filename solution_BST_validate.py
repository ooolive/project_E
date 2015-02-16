#coding=utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(root):
    ret = [ ]
    if root == None:
        return ret

    ret.extend(helper(root.left))
    ret.append(root.val)
    ret.extend(helper(root.right))
    return ret

class Solution_initial:
    def isValidBST(self, root):
        if root == None:
            return True
        ret = helper(root)
        p = ret[0]-1
        for i in ret:
            if i <= p:
                return False
            p = i
        return True

# initial solution, 不快不慢，但是没啥技术含量

class Solution:
    def isValidBST(self, root):
        cmp = -pow(2, 32)
        t = [ ]
        ptr = root
        while 1:
            while ptr:
                t.append(ptr)
                ptr = ptr.left
            if len(t) == 0:
                break
            ptr = t.pop()
            if ptr.val <= cmp:
                return False
            cmp, ptr = ptr.val, ptr.right

        return True

# 迭代 O(1) 空间实现，都是 in-order DFS
# 参考 http://www.cnblogs.com/kangyoung/articles/2168069.html
# 发现自己竟然不会迭代实现...

# 141229

s = Solution()

t = None
print(s.isValidBST(t))

t = TreeNode(1)
print(s.isValidBST(t))

t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.left.right = TreeNode(5)

print(s.isValidBST(t))

t = TreeNode(0)
t.left = TreeNode(-1)
print(s.isValidBST(t))

t = TreeNode(0)
t.right = TreeNode(-1)
print(s.isValidBST(t))
