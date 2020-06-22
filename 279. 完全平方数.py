# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 动态规划法
# 使用一个数组保存到当前数的最少组成方法
# 遍历到该数时 首先将该数设为本身 如5最多可以（1+1+1+1+1）5次组成
# 之后往5之前的可以平方的数查找 如1+2*2 则比较5和（1记录的次数+1）比较大小 取小的那个记录

# On√n
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0 for i in range(n+1)]
        for _ in range(1,n+1):
            arr[_] = _
            j = 1
            while _ - j**2 >=0:
               arr[_] = min(arr[_], arr[_ - j**2]+1)
               j+=1
        return arr[n]

a = Solution()
a.numSquares(5)