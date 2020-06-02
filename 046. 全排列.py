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
