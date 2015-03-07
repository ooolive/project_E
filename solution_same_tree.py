
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None

def foundation_initial(x, y):
    if (x or y) and not (x and y):
        return False
    elif not (x or y):
        return True
    if x.val != y.val:
        return False
    if (x.left or x.right or y.left or y.right) == None:
        return True
    return foundation(x.left, y.left) and foundation(x.right, y.right)

def foundation(x, y):
    if not (x or y):
        return True
    elif not (x and y):
        return False
    return x.val == y.val and foundation(x.left, y.left) and foundation(x.right, y.right)

class Solution:
    def isSameTree(self, p, q):
        return foundation(p, q)

# 很简单的一道题，凑数用的，不过速度总是提不上去...
# 可以 iterative, 但是感觉很蛋疼
# recursive 没准也能 one-line, 不过也不够 Pythonic

# 150307 EVE

s = Solution()
print(s.isSameTree(None, None))
print(s.isSameTree(None, TreeNode(1)))
print(s.isSameTree(TreeNode(1), TreeNode(1)))
print(s.isSameTree(TreeNode(1), TreeNode(0)))
