# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#  
#
# 示例 1:
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#遍历数组时计算当前最大值，不断更新
# 令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
# 由于存在负数，那么会导致最大的变最小的，最小的变最大的。
# 因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
# 当负数出现时则imax与imin进行交换再进行下一步计算
# 时间复杂度：O(n)O(n)
# 
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        max_ans = 1
        min_ans = 1
        for _ in nums:
            if _ < 0:
                max_ans, min_ans = min_ans, max_ans
            max_ans = max(max_ans * _, _)
            min_ans = min(min_ans * _, _)

            ans = max(ans, max_ans)
        return ans



class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDp = [nums[0]]
        minDp = [nums[0]]
        for i in nums[1:]:
            tmp = (i*maxDp[-1], i*minDp[-1], i)
            maxDp.append(max(tmp))
            minDp.append(min(tmp))
        return max(maxDp)

