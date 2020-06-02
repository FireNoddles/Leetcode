# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/spiral-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix ==[]:
            return []
        up = 0
        down = len(matrix)
        left = 0
        right = len(matrix[0])
        res = []
        while(1):
            for _ in range(left,right):
                res.append(matrix[up][_])
            up+=1
            if up >= down:
                break
            for _ in range(up,down):
                res.append(matrix[_][right-1])
            right-=1
            if right <= left:
                break
            for _ in range(right-1,left-1,-1):
                res.append(matrix[down-1][_])
            down-=1
            if down <= up:
                break
            for _ in range(down-1,up-1,-1):
                res.append(matrix[_][left])
            left+=1
            if left >= right:
                break
        return res