# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 处理连续子串问题 双指针 前缀和
#因为有负数存在 所以双指针太复杂

#前缀和 On^2 等同于暴力法 超时
class Solution(object):
    def subarraySum(self, nums, k):
        ans = 0
        s = [0 for i in range(len(nums)+1)]
        s[0] = 0
        for i in range(1, len(nums)+1):
            s[i] = s[i-1] +nums[i-1]
        for i in range(1,len(nums)+1):
            for j in range(i):
                if (s[i] - s[j]) == k:
                    ans+=1
        return ans

# 优化 带字典的前缀和 On
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        s = 0
        ans = 0
        for i in range(len(nums)):
            s += nums[i]
            if s == k:
                ans+=1
            if s-k in d:
                ans+=d[s-k]
            if s in d:
                d[s]+=1
            else:
                d[s] =1
        return ans