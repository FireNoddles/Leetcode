# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#  
#
# 示例 :
# 给定二叉树
#
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.m = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.help(root)
        return self.m

    def help(self, root):
        if root == None:
            return 0
        r = self.help(root.right)
        l = self.help(root.left)
        self.m = max(self.m, r + l)
        return max(l, r) + 1

