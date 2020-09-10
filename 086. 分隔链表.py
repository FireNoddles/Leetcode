# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/partition-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 额外数组 空间ON 时间复杂度On
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        arr_s = []
        arr_m = []
        while head:
            if head.val < x:
                arr_s.append(head.val)
            else:
                arr_m.append(head.val)
            head = head.next
        t = ListNode(-1)
        p = t
        for _ in arr_s:
            temp = ListNode(_)
            p.next = temp
            p = p.next
        for _ in arr_m:
            temp = ListNode(_)
            p.next = temp
            p = p.next
        return t.next
# 双链表 On复杂度 o1空间
class Solution2(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        arr_s = ListNode(-1)
        ans = arr_s
        arr_m = ListNode(-1)
        ans_t = arr_m
        while head:
            if head.val < x:
                arr_s.next = head
                arr_s = arr_s.next
            else:
                arr_m.next = head
                arr_m = arr_m.next
            head = head.next
        # 末尾至空 否则可能循环
        arr_m.next = None
        arr_s.next = ans_t.next
        return ans.next
arr = [1,4,3,2,5,2]
head = ListNode(None)
p = head
for _ in arr:
    t = ListNode(_)
    head.next = t
    head = head.next

a = Solution2()
r = a.partition(p.next, 3)
while r:
    print(r.val)
    r = r.next