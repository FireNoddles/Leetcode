# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(None)
        result = node
        flag = 0
        while l1 and l2:
            temp = l1.val + l2.val
            if flag:
                temp += 1
                flag = 0
            if temp >= 10:
                flag = 1
                temp -= 10
            node.val = temp
            if l1.next and l2.next:
                node2 = ListNode(None)
                node.next = node2
                node = node.next
            l1 = l1.next
            l2 = l2.next
        if l1: self.deal(l1, flag, node)
        elif l2: self.deal(l2, flag, node)
        else:
            if flag:
                node2 = ListNode(flag)
                node.next = node2
        return result

    def deal(self, l1, flag, node):
        while l1:
            if flag:
                l1.val += 1
                if l1.val >= 10:
                    l1.val -= 10
                else:
                    flag = 0
                node2 = ListNode(l1.val)
                node.next = node2
                node = node.next
                l1 = l1.next
            else:
                node2 = ListNode(l1.val)
                node.next = node2
                node = node.next
                l1 = l1.next
        if flag:
            node2 = ListNode(flag)
            node.next = node2
        return

# 简洁版 主要是在一个链表走到头之后 将其设为0 与后续的链表相加
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        result = node
        flag = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            temp = l1.val + l2.val + flag
            if temp >= 10:
                flag = 1
                temp -= 10
            else:flag = 0
            node2 = ListNode(temp)
            node.next = node2
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if flag > 0:
            node2 = ListNode(flag)
            node.next = node2
        return result.next

l1 = ListNode(9)
l1.next = ListNode(9)
l2 =ListNode(1)
a = Solution()
print(a.addTwoNumbers(l1,l2).val)