# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def __init__(self):
        self.ans = []
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.help(nums,0)
        return self.ans
    def help(self,nums,index):
        nums = nums[:]
        if index == len(nums)-1:
            self.ans.append(nums)
            return
        for i in range(index,len(nums)):
            nums[i],nums[index] = nums[index],nums[i]
            self.help(nums,index+1)
            nums[i],nums[index] = nums[index],nums[i]

a= Solution()
print(a.permute([1,2,3]))
