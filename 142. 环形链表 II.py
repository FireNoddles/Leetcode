# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
# 说明：不允许修改给定的链表。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        n = head
        while n!=None:
            p = p.next
            if n.next:
                n = n.next.next
            else:
                return None
            if p==n:
                break
        if n==None:
            return None
        else:
            t= head
            while t != p:
                t = t.next
                p=p.next
        return t
