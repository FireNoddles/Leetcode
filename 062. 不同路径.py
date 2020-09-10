# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 递归 超时
class Solution(object):
    def __init__(self):
        self.res = 0
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.help(m, n, 0, 0)
        return self.res
    def help(self, m, n, i, j):
        if i == m-1 and j==n-1:
            self.res+=1
            return
        if i > m-1 or j>n-1:
            return
        self.help(m, n, i+1, j)
        self.help(m, n, i, j+1)


# 动态规划 Omn Omn
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for i in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
