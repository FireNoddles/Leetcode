# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。


# 哈希 On
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for _ in nums:
            if _ not in dic:
                dic[_] = 1
            else:
                return True
        return False


# set
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums2 = set(nums)
        return True if len(nums2) != len(nums) else False