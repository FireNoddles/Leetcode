# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                obstacleGrid[0][i] = 1
            else:
                while i < len(obstacleGrid[0]):
                    obstacleGrid[0][i] = 0
                    i += 1
                break
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                while i < len(obstacleGrid):
                    obstacleGrid[i][0] = 0
                    i += 1
                break
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]