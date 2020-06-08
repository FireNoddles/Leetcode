# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ans = []
        stack = [root]
        i = 1
        while stack :
            temp = []
            next_stack = []
            while stack:
                a = stack.pop()
                temp.append(a.val)
                if i%2 ==1:
                    if a.left:
                        next_stack.append(a.left)
                    if a.right:
                        next_stack.append(a.right)
                else:
                    if a.right:
                        next_stack.append(a.right)
                    if a.left:
                        next_stack.append(a.left)
            ans.append(temp)
            stack = next_stack[:]
            i+=1
        return ans