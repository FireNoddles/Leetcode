# 350. 两个数组的交集 II
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        return self.help(nums2, nums1) if len(nums1) < len(nums2) else self.help(nums1, nums2)

    def help(self, nums1, nums2):
        ans = []
        for _ in nums2:
            if _ in nums1:
                ans.append(_)
                nums1.remove(_)
        return ans

