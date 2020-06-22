# 给定一个无序的整数数组，找到其中最长上升子序列的长度。

# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。


#dp omn
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums ==[]:
            return 0
        arr = [1 for i in range(len(nums))]
        max_ans= 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    arr[i]= max(arr[j]+1,arr[i])
                    max_ans = max(max_ans, arr[i])
        return max_ans