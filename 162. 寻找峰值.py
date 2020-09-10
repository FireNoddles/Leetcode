# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-peak-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 首先分析一下情况，如果 mid 一直比右侧的数小，那么 mid 处的值肯定不是峰值。
# 可以看到，如果 nums[mid]>nums[mid+1]，那么峰值一定在左侧
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else: return 1
        i = 0
        j = len(nums) -1
        # 注意不是小于等于 因为j=mid
        while i<j:
            mid = (i+j) //2
            if nums[mid] > nums[mid+1]:
                j = mid
            else:
                i = mid + 1
        return i