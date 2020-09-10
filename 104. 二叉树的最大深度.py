# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        ans = self.help(root)
        return ans
    def help(self, root):
        if root == None:
            return 0
        left = 1 + self.help(root.left)
        right = 1 + self.help(root.right)
        return max(left,right)