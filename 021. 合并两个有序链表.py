# 将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        i = l1
        j = l2
        head = ListNode(None)
        p = head
        while i and j:
            if i.val<=j.val:
                p.next= i
                i = i.next
                p = p.next
            else:
                p.next= j
                j = j.next
                p = p.next
        if i:
            p.next = i
        if j:
            p.next = j
        return head.next



