# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

# 输入: head = [4,5,1,9], node = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/delete-node-in-a-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 我们无法访问我们想要删除的节点 之前 的节点，我们始终不能修改该节点的 next 指针。
# 相反，我们必须将想要删除的节点的值替换为它后面节点中的值，然后删除它之后的节点。
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next