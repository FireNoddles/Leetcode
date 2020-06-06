# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.help(root)
    def help(self,root):
        if root==None:
            return True
        a = self.help(root.left)
        b = self.help(root.right)
        if a and b:
            if not root.left and not root.right:
                return True
            elif root.left and not root.right:
                if root.left.val < root.val:
                    return True
            elif root.right and not root.left:
                if root.right.val > root.val:
                    return True
            elif root.right.val > root.val and root.left.val < root.val:
                    return True
            else:
                return False
        else:
            return False
