# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        return str(bin(a+b)).replace('0b','')