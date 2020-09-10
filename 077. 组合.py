# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combinations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# https://leetcode-cn.com/problems/combinations/solution/xiong-mao-shua-ti-python3-hui-su-jian-zhi-by-lot-2/
class Solution(object):
    def __init__(self):
        self.ans = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        arr = [i + 1 for i in range(n)]
        if n == k:
            return [arr]
        self.help(arr, k, [])
        return self.ans

    def help(self, arr, k, temp):
        if len(temp) == k:
            self.ans.append(temp[:])
            return
        for _ in range(len(arr)):
            if temp and arr[_] < temp[-1]:# 剪枝 不能出现逆序
                continue
            temp.append(arr[_])
            self.help(arr[:_] + arr[_ + 1:], k, temp)
            temp.pop()