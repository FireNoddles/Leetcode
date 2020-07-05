import socket
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-sum-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 使用一个列表存头结点 到当前节点每一层的和
class Solution(object):
    def __init__(self):
        self.ans =0
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.help([], root, s)
        return self.ans
    def help(self,temp,root,s):
        arr = temp[:]
        if root == None:
            return
        for _ in range(len(arr)):
            arr[_] += root.val
        arr.append(root.val)
        for _ in arr:
            if _ == s:
                self.ans+=1
        self.help(arr, root.left, s)
        self.help(arr, root.right, s)
