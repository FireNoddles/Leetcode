# 给定一个 m x n 的矩阵，如果一个元素为 0，
# 则将其所在行和列的所有元素都设为 0。请使用原地算法

class Solution(object):
    @classmethod
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        dic_row = {}
        dic_col = {}
        for _ in range(len(matrix)):
            if _ not in dic_row:
                dic_row[_] = 1
            for __ in range(len(matrix[0])):
                if __ not in dic_col:
                    dic_col[__] = 1
                if matrix[_][__]==0:
                    dic_row[_]=0
                    dic_col[__]=0
        for _ in range(len(matrix)):
            for __ in range(len(matrix[0])):
                if dic_row[_] * dic_col[__] == 0:
                    matrix[_][__]=0
        print(matrix)
Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])