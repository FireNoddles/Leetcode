# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
#
#  
#
# 示例 1:
#
# 输入: [3,0,1]
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/missing-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#O2n O1求和方式
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = 0
        for _ in range(len(nums)+1):
            target+=_
        fact = sum(nums)
        return target - fact


# On O1方式
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for _ in range(len(nums)+1):
            if _ not in nums:
                return _