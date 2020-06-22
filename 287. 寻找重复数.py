# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-duplicate-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 转换成环的问题 快慢指针
# 以数组中存的数为下一个结点的位置 如果存在重复数 那么就会有环

# 找到相遇点 让新指针从头开始找 和slow相遇的点就是入口（重复的数） On
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        c = 0
        while 1:
            slow = nums[slow]
            c = nums[c]
            if  c == slow :
                break
        return slow