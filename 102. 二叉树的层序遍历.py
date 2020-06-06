# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root ==None:
            return []
        ans = []
        layer = []
        temp = [root]
        while len(temp)>0:
            temp2 = []
            layer = []
            for _ in range(len(temp)):
                a = temp[_]
                if a.left:
                    temp2.append(a.left)
                if a.right:
                    temp2.append(a.right)
                layer.append(a.val)
            ans.append(layer[:])
            temp = temp2[:]
        return ans