# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#  
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/product-of-array-except-self
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 剑指offer 倒三角方法
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]
        for _ in range(0,len(nums)-1):
            res.append(res[-1]*nums[_])
        temp = 1
        for _ in range(len(nums)-1, -1,-1):
            res[_] = res[_]*temp
            temp = temp * nums[_]
        return res