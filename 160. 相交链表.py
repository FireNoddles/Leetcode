# 编写一个程序，找到两个单链表相交的起始节点。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next

        if not p1:
            p1 = headB
        else:
            p2 = headA

        while p1 and p2:
            p1 = p1.next
            p2 = p2.next

        if not p1:
            p1 = headB
        else:
            p2 = headA

        while p1 and p2:
            if id(p1) == id(p2):
                return p1
            p1 = p1.next
            p2 = p2.next
        return None