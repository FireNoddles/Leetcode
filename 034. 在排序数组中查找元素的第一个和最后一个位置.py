# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 口诀：查值直接就返回 查左收右不返回 查右收左不返回 左右别忘查越界
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = self.help(nums, target,0)
        b = self.help(nums, target,1)
        if a!=-1 and b!=-1:
            return [a,b]
        else:
            return [-1,-1]
    def help(self, nums, target,flag):
        i = 0
        j = len(nums) - 1
        while i<=j:
            mid = (i+j)//2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid -1
            elif nums[mid] == target and flag == 0:
                j = mid - 1
            elif nums[mid] == target and flag == 1:
                i= mid + 1
        if flag == 0:
            if i > len(nums)-1 or nums[i]!=target:
                return -1
            else:
                return i
        if flag == 1 :
            if j < 0 or nums[j]!=target:
                return -1
            else:
                return j

a= Solution()
a.search([5,7,7,8,8,10],8)