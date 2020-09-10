# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
#
#  
#
# 示例：
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# 返回 13。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 堆排序
heap = []
# from heapq import * 
#3进堆 heappush(heap, 3)
# heappop(heap) 取堆顶最小元素
#heapreplace(heap, x)  取堆顶最小元素，并将x放入堆



# 折半查找Onlogmax-min
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        low = matrix[0][0]
        n = len(matrix)
        high = matrix[n-1][n-1]
        while low < high:
            mid = (low + high)//2
            c = self.help(matrix,mid, n)
            if c<k:
                low = mid+1
            else:
                # 因为有可能c==k 因为mid有可能不在矩阵之中 所以最后返回high
                high = mid
        return high
    def help(self, matrix, target, length):
        i = 0
        j = length - 1
        count = 0
        while i<=length-1 and j>=0:
            if matrix[i][j]<=target:
                #这一行都小于目标 所以加j+1
                count+= (j+1)
                i+=1
            else:
                j-=1
        return count

