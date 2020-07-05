# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。

# O（1）复杂度 因为整形的长度是固定的
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x>0 or y>0:
            if x&1 != y&1:
                ans+=1
            x = x>>1
            y = y>>1
        return ans
