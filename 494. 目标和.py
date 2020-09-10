# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
#
#  
#
# 示例：
#
# 输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 一共有5种方法让最终目标和为3。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/target-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 递归超时
class Solution(object):
    def __init__(self):
        self.ans = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.help(nums,S,0,0)
        return self.ans
    def help(self,nums,S,index,arr):
        if index == len(nums)-1:
            if (arr+nums[-1])==S:
                self.ans+=1
            if (arr-nums[-1])==S:
                self.ans+=1
            return
        arr = arr + nums[index]
        self.help(nums,S,index+1,arr)
        arr = arr - 2*nums[index]
        self.help(nums,S,index+1,arr)


# dp
# 动态规划：题意求方法数，所以dp[i][j]表示从0-i数组中可以通过加减得到结果j的方法数量
# j取值范围-sum（nums）到sum（nums）
# 状态转移方程：
# 对于j如果nums[i]使用+号，则dp[i][j]=dp[i-1][j-nums[i]]=r的方法数量
# 对于j如果nums[i]使用-号，则dp[i][j]=dp[i-1][j+nums[i]]=l的方法数量
# 所以综上，dp[i][j]方法总数为l+r,即：
# dp[i][j] = dp[i-1][j-nums[i]]+dp[i-1][j+nums[i]]
# 目标位置:dp[n-1][sums+S]

# 类似硬币找零钱有多少种组合方法
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [[0 for i in range(-sum(nums), sum(nums) + 1)] for i in range(len(nums))]
        dp[0][sum(nums) - nums[0]] += 1
        dp[0][sum(nums) + nums[0]] += 1
        le = sum(nums)
        if S > le or S < -le:
            return 0
        for i in range(1, len(nums)):
            for j in range(0, 2 * le + 1):
                if j - nums[i] < 0:
                    l = 0
                else:
                    l = dp[i - 1][j - nums[i]]
                if j + nums[i] > 2 * le:
                    r = 0
                else:
                    r = dp[i - 1][j + nums[i]]

                dp[i][j] = l + r
        return dp[len(nums) - 1][sum(nums) + S]

a = Solution2()
a.findTargetSumWays([1,1],2)

