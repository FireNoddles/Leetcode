# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 使用双指针 使得i和j之间都是0 当i不为0时 和j交换
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        while nums[j]!=0:
            j+=1
            if j == len(nums):
                return
        for i in range(j+1,len(nums)):
            if nums[i]!=0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1

# 冒泡
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = []
        for i in range(1, len(nums)):
            for j in range(0, len(nums) - i):
                if nums[j] == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


a = Solution()
a.moveZeroes(
[0,0,1])