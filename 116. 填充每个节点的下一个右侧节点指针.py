# 给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 递归
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return None
        self.help(root.left,root.right)
        return root
    def help(self, left, right):
        if not left:
            return
        left.next = right
        self.help(left.left,left.right)
        self.help(left.right,right.left)
        self.help(right.left,right.right)


# 用队列也可以 会快 按层进队列 挨个next