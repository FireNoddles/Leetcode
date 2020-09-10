# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#  
#
# 示例 1:
#
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/number-of-islands
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def __init__(self):
        self.flag = []
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.flag = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and self.flag[i][j] == 0:
                    count +=1
                    self.help(grid,i,j)
        return count
    def help(self, grid,i,j):
        if i<0 or i >=len(grid) or j<0 or j >=len(grid[0]) or grid[i][j] == '0' or self.flag[i][j]==1:
            return
        else:
            if grid[i][j] == '1':
                self.flag[i][j] = 1
                self.help(grid,i-1,j)
                self.help(grid,i+1,j)
                self.help(grid,i,j-1)
                self.help(grid,i,j+1)