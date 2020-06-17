# 反转一个单链表。


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        p = head
        last = p
        while p:
            last = last.next
            p.next = pre
            pre = p
            p = last
        return pre
