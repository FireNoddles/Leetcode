# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/majority-element
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 排序 中间位置的肯定是多的ologn
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return nums[len(nums)//2]

# 投票法 数出现多的一定留到最后
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = 0
        ans = nums[0]
        for _ in nums:
            if _ == ans:
                num+=1
            else:
                num-=1
                if num == 0:
                    ans = _
                    num = 1
        return ans
