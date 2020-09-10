
#实际上是统计5和其倍数出现的个数 因为5乘以其它数有0   例如5,10,15,20.....
#而当为25时 可以拆成2个5需要多加一次5
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n>0:
            ans+=n/5
            #每次循环缩5 相当于第二次while 是ans+=n/25 第三次是ans+=n/125
            n = n/5

        return ans


a = Solution()
a.trailingZeroes(30)