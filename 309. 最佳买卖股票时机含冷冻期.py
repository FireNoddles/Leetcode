# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        dp = [[0 for i in range(3)] for i in range(len(prices))]
        # 0卖出后的收益
        dp[0][0] = 0
        # 1没有股票情况的收益 （两种 第一种是前一天没有股票，或是前一天卖出了，进入冷冻期）
        dp[0][1] = 0
        # 2持有股票的收益
        dp[0][2] = - prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = dp[i-1][2] + prices[i]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]- prices[i])
        return max(dp[i][0], dp[i][1])