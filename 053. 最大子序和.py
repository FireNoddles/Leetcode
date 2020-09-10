#给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 双指针 当两个指针之间的和小于0时 左指针等于右指针 递加
# 使用动态规划更方便
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if len(nums) == 1:
#             return nums[0]
#
#         i = 0
#         j = 1
#         temp = nums[i]
#         max_num = nums[i]
#         while j < len(nums):
#             if temp < 0:
#                 i = j
#                 j += 1
#                 temp = nums[i]
#             else:
#                 temp += nums[j]
#                 j += 1
#             max_num = max(temp, max_num)
#
#         return max_num


# 动态规划
# sum_ans 为加上当前数字的和 如果sumans<0 则当前数加上sumans没有帮助 将它直接等于当前数
# 记录每一步之后的maxans
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        sum_ans = 0
        for _ in range(len(nums)):
            if sum_ans<0:
                sum_ans = nums[_]
            else:
                sum_ans += nums[_]
            ans = max(sum_ans, ans)
        return ans