# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0 or x ==1:
            return 1
        flag = 0
        if n < 0:
            flag = 1
            n = abs(n)
        temp = 1
        re = 1
        c = n
        while n > 0:
            if c ==n:
                temp = x
            else:
                temp = temp * temp
            a = n & 1
            if a:
                re *= temp
            n = n >> 1
        if flag >0:
            return 1/re
        return re

a= Solution()
print(a.myPow(2,4))