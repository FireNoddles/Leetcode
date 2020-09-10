# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#  
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 定一个数 从他之后开始双指针
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = sum([nums[i] for i in range(3)])
        for i in range(0,len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                s = sum([nums[j] for j in [i,l,r]])
                if s == target:
                    return target
                ans = s if abs(target - s) < abs(target - ans) else ans
                r = r-1 if s > target else r
                l = l+1 if s < target else l
        return ans
