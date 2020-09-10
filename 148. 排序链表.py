# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4

# 注意栈用了logn空间 链表的二路归并

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        p1 = head
        p2 = head
        while p1 and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if not p2.next:
                break
        mid = p1
        p1 = p1.next
        mid.next = None
        L = self.sortList(head)
        R = self.sortList(p1)
        return self.merge(L, R)

    def merge(self, L, R):
        cur = ListNode(None)
        ans = cur
        while L and R:
            if L.val < R.val:
                cur.next = L
                L = L.next
            else:
                cur.next = R
                R = R.next
            cur = cur.next
        if L:
            cur.next = L
        else:
            cur.next = R
        return ans.next



