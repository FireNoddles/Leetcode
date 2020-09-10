# 首先11比3大，结果至少是1， 然后我让3翻倍，就是6，
# 发现11比3翻倍后还要大，那么结果就至少是2了，那我让这个6再翻倍，
# 得12，11不比12大，吓死我了，差点让就让刚才的最小解2也翻倍得到4了。
# 但是我知道最终结果肯定在2和4之间。也就是说2再加上某个数，
# 这个数是多少呢？我让11减去刚才最后一次的结果6，剩下5，我们计算5是3的几倍，
# 也就是除法，看，递归出现了
#
# 作者：liujin-4
# 链接：https://leetcode-cn.com/problems/divide-two-integers/solution/po-su-de-xiang-fa-mei-you-wei-yun-suan-mei-you-yi-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 0
        if dividend < 0:
            dividend = -dividend
            flag += 1
        if divisor < 0:
            divisor = -divisor
            flag += 1
        if divisor == 1:
            if flag ==1:
                if dividend > 2**31:
                    return 2**31-1
            else:
                if dividend > 2**31-1:
                    return 2**31-1
        re = self.help(dividend, divisor)
        if flag ==1:
            return -re
        else:
            return re
    def help(self,dividend, divisor):
        if dividend < divisor:
            return 0
        temp = divisor
        result = 1
        while temp+temp <= dividend:
            temp += temp
            result += result
        return result + self.help(dividend - temp, divisor)