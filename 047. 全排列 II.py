# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def __init__(self):
        self.ans = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.help(0, nums)
        return self.ans

    def help(self, index, nums):

        if index == len(nums) and nums not in self.ans:
            self.ans.append(nums[:])
            return

        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.help(index + 1, nums)
            nums[i], nums[index] = nums[index], nums[i]
