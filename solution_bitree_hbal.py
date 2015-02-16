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

# ��ô���濴�Ų���
# ����ָ���û�취��...
# initial solution ����̫��
# ���� WA �˺ü���
# ע����Ŀ������ a height-balanced binary tree is defined as a binary
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

# Solution 2 ����� https://oj.leetcode.com/discuss/12331/accepted-o-n-solution
# ɥ�Ĳ���İ� balanced ���ϵ��� depth ����
# �������Ԫ�����˷��ص���ֵ��ò�ƿ��˲���
# ������ helper �����ֲ���֮����Ȼ�ɾ������ǻ���� recursion limit ������
# discussion ����ò��Ҳ�����ᵽ�ˣ�����ȫ�ֵ� helper �� AC ��
# �ѵ��� Python �Ĵ���������

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
