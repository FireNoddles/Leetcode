# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-a-2d-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)):
            if target <= matrix[i][len(matrix[0]) - 1]:
                break

        arr = matrix[i]
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = l + r >> 1
            if arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                return True
        return False
# 改进点 在定位行时也可以二分定位