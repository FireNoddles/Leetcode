# 给定一个二叉树，检查它是否是镜像对称的。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root ==None:
            return True
        return self.help(root.left,root.right)
    def help(self, left, right):
        if not left and not right:
            return True
        if (left and not right) or (not left and right) or (left.val != right.val):
            return False
        else:
            return self.help(left.left, right.right) and self.help(left.right, right.left)