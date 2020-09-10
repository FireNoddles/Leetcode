# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 转列表 双指针
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        i = 0
        j = len(arr)-1
        while j-i >= 1:
            if arr[i] !=arr[j]:
                return False
            i+=1
            j-=1
        return True
