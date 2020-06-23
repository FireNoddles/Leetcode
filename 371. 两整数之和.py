# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

class Solution:
    def Add(self, a, b):
        while(b):
            # 0xFFFFFFFF 对负数的处理 使其不越界 不可拆开写 如
            #
            #             a = (a ^ b) & 0xFFFFFFFF
            #             b = ((a & b) <<1) & 0xFFFFFFFF
            # 可写成：
            # c = ((a & b) << 1) & 0xFFFFFFFF
            # a = (a ^ b) & 0xFFFFFFFF
            # b = c
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)