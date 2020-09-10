# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/jump-game
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 1 递归（超时）
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <=1:
            return True
        return self.help(nums,0)
    def help(self,nums, index):
        if index >= len(nums)-1:
            return True
        if nums[index] == 0:
            return False
        for i in range(nums[index],0,-1):
            temp = self.help(nums, index+i)
            if temp:
                return True
        return False


# 贪心 记录每个位置可以到达的最大值 如果最大值大于数组长度 返回成功
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        max_jump = nums[0]
        for i in range(1, len(nums)):
            if max_jump >= len(nums)-1:
                return True
            elif i <= max_jump:
                max_jump = max(nums[i]+i, max_jump)
        return False
