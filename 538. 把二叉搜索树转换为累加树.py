# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
#
#  
#
# 例如：
#
# 输入: 原始二叉搜索树:
#               5
#             /   \
#            2     13
#
# 输出: 转换为累加树:
#              18
#             /   \
#           20     13
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/convert-bst-to-greater-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.s = 0

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.help(root)
        return root

    def help(self, root):
        if root == None:
            return
        self.help(root.right)
        self.s += root.val
        root.val = self.s

        self.help(root.left)