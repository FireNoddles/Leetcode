# 动态规划
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr = [1 for i in range(len(nums))]
        for i in range(1,len(nums)):
            temp = []
            for j in range(0,i):
                if nums[i] > nums[j]:
                    temp.append(arr[j]+1)
            if temp!=[]:
                arr[i] = max(temp)
            if arr[i] >=3:
                return True
        return False

# 维护两个标记 第一个为最小的 第二个为第二小的
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        one_min = sys.maxsize
        sec_min = sys.maxsize

        for i in range(len(nums)):
            # 如果比第一个还小 更新第一个 不更新第二个 原因是
            # 如果后续出来一个数比第二个还大 则说明成功
            # 如果出来一个比第二个数还小 再更新第二个
            if nums[i] <= one_min:
                one_min = nums[i]
            elif nums[i] <= sec_min:
                sec_min = nums[i]
            elif nums[i] > sec_min:
                return True
        return False
a = Solution()
a.increasingTriplet([5,4,3,2,1])