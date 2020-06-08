# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:
            return []
        return self.help(preorder, inorder)
    def help(self, preorder, inorder):
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        node = TreeNode(preorder[0])
        partition = inorder.index(preorder[0])
        node.left = self.help(preorder[1:partition+1], inorder[:partition])
        node.right = self.help(preorder[partition+1:], inorder[partition+1:])
        return node