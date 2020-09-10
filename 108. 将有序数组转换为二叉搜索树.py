# Definition for a binary tree node.将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return []
        a = self.help(nums)
        return a

    def help(self,nums):
        if len(nums) == 0:
            return None
        partition = (len(nums)-1)//2
        node = TreeNode(nums[partition])
        node.left = self.help(nums[:partition])
        node.right = self.help(nums[partition+1:])
        return node

a = Solution()
print(a.sortedArrayToBST(
[-10,-3,0,5,9]))