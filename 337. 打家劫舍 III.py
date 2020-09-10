# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
#
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
#
# 示例 1:
#
# 输入: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 必须要使用字典 记录每个节点的父节点在偷/不偷的状态下的值
        # 第二次调用的时候直接查找词典 返回值 节省再次调用时间
        dic = {}
        def help(root, sign):
            if root == None:
                return 0
            if (root, sign) in dic:
                return dic[root, sign]
            # a上一层没偷 这一层偷
            # c 这一层不偷(上一层偷了 这一层不偷 上一层没偷 这一层不偷）
            a,c = 0,0
            if sign==0:
                a = help(root.left, 1)+ help(root.right, 1) + root.val
            c = help(root.left, 0)+ help(root.right, 0)
            dic[root,sign] = max(a,c)
            return max(a,c)
        return help(root,0)



