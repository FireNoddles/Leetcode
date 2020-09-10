# 类似于剑指 求最小数

# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例 1:
#
# 输入: [10,2]
# 输出: 210


# 冒泡排序 On^2

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        ans = ''
        for i in range(1, len(nums)):
            for j in range(0, len(nums) - i):
                if str(nums[j]) + str(nums[j+1]) < str(nums[j+1]) + str(nums[j]):
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
        if nums[0] == 0:
            return '0'
        for _ in nums:
            ans+= str(_)

        return ans
