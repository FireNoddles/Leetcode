# 给定一个二叉树，原地将它展开为一个单链表。
#
#  
#
# 例如，给定二叉树
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#从下往上调整 每次找结点p的左子树的最右结点接上p的右孩子
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.help(root)
    def help(self, root):
        if root == None:
            return
        self.help(root.left)
        self.help(root.right)
        if root.left!=None:
            p = root.left
            while p.right:
                p = p.right
            p.right = root.right
            root.right = root.left
            root.left = None