# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.help(root)
        for i in range(1,len(self.ans)):
            if self.ans[i] <= self.ans[i-1]:
                return False
        return True
    def help(self,root):
        if root == None:
            return
        self.help(root.left)
        self.ans.append(root.val)
        self.help(root.right)
