# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 中序遍历
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root==None:
            return []
        que = []
        self.help(que,root,k)
        return que[k-1]
    def help(self,que,root,k):
        if root == None or len(que)==k:
            return
        self.help(que,root.left,k)
        que.append(root.val)
        self.help(que,root.right,k)