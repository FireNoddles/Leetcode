#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4


# dp 一个位置如果为1，和它的左边 上面 和左上角三个位置有关 取三个位置的最小值+1

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        if len(matrix)==1:
            return 1 if '1'in matrix[0] else 0

        max_ans = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j]=='1':
                    if i==0 or j ==0:
                        matrix[i][j] == 1
                    else:
                        temp = min(min(int(matrix[i-1][j]),int(matrix[i][j-1])),int(matrix[i-1][j-1]))
                        matrix[i][j] = int(temp) + 1
                    max_ans = max(int(matrix[i][j]),max_ans)
        return max_ans**2 