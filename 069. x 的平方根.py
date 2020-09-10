# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sqrtx
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 4:
            return 1
        a = self.help(x, x//2)
        for _ in range(a, a*2+1):
            if _**2<=x and (_+1) ** 2 > x:
                return _
    def help(self, x, num):
        if num**2 <=x:
            return num
        else:
            a = self.help(x, num//2)
        return a


# 折半查找

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        if x < 4:
            return 1
        i = 0
        j = x
        mid = (i+j) //2
        ans = mid
        while i <= j:
            # 因为要找最大的那个mid 及时记录 并增大mid
            if mid**2 < x:
                ans = mid
                i = mid+1
            elif mid **2 >x:
                j = mid -1
            else:
                ans = mid
                break
            mid = (i+j) //2
        return ans