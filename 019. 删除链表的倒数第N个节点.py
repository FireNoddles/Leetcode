# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return False
        i = head
        j = head
        pre = ListNode(0)
        pre.next = head
        while n > 1:
            if j.next:
                j = j.next
            else:
                return False
            n-=1
        while j.next:
            j = j.next
            i = i.next
            pre = pre.next
        pre.next = i.next
        if i == head:
            head = pre.next
        return head