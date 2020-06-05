class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr = [0,0,0]
        for _ in nums:
            if _ == 0:
                arr[0]+=1
            elif _==1:
                arr[1]+=1
            else:
                arr[2]+=1
        i = 0
        for _ in range(3):
            for __ in range(arr[_]):
                print(i)
                nums[i] = _
                i+=1
# 三指针 一次遍历

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i =0
        j = len(nums) -1
        m = 0
        while m <= j:
            if nums[m] == 0:
                nums[m],nums[i] = nums[i],nums[m]
                i+=1
                m+=1
            elif nums[m] ==1:
                m+=1
            else:
                nums[m],nums[j] = nums[j],nums[m]
                j-=1
Solution().sortColors(
[2,0,2,1,1,0])