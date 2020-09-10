# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.proad=[]
        self.qroad = []
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return False
        self.help(root,p,q,[])

        if len(self.proad)>len(self.qroad):
            for i in range(len(self.proad)-1, -1, -1):
                if self.proad[i] in self.qroad:
                    return self.proad[i]
        else:
            for i in range(len(self.qroad)-1, -1, -1):
                if self.qroad[i] in self.proad:
                    return self.qroad[i]


    def help(self, root,p,q, t):
        temp = t[:]
        if (len(self.proad)!=0 and len(self.qroad)!=0) or not root :
            return
        temp.append(root)
        if root.val == p.val:
            self.proad.extend(temp)
        if root.val == q.val:
            self.qroad.extend(temp)
        self.help(root.left,p, q, temp)
        self.help(root.right,p, q, temp)
