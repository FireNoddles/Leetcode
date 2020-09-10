# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# On个辅助单元
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for _ in nums:
            if _ not in dic:
                dic[_] = 1
            else:
                dic[_]+=1
        for _ in dic:
            if dic[_]==1:
                return _

#使用异或 一个数异或本身为0 O1个辅助单元 前提是别的数都出现偶数次

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        for _ in nums:
            temp = temp^ _
        return temp