#给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

# 如果小数部分为循环小数，则将循环的部分括在括号内。
#
# 示例 1:
#
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 示例 2:
#
# 输入: numerator = 2, denominator = 1
# 输出: "2"
# 示例 3:
#
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = ''
        if numerator==0:
            return '0'
        if (numerator<0 and denominator >0):
            ans += '-'
            numerator = -numerator
        if (numerator>0 and denominator<0):
            ans += '-'
            denominator = -denominator
        if (numerator<0 and denominator<0):
            numerator = -numerator
            denominator = -denominator
        if numerator == denominator:
            return '1'
        elif numerator > denominator:
            temp = numerator // denominator
            if temp * denominator == numerator:
                return ans+str(temp)
            else:
                ans = ans + str(temp) + '.'
                numerator -= (temp * denominator)
                s = self.help(numerator, denominator)
                return ans + s
        else:
            ans+='0.'
            s = self.help(numerator, denominator)
            return ans + s
    def help(self, numerator, denominator):
        old = []
        ans = ''
        numerator *= 10
        old.append(numerator)
        while 1:
            temp = numerator // denominator
            ans += str(temp)
            if temp * denominator == numerator:
                return ans
            elif temp != 0:
                numerator -= (temp * denominator)
                numerator *= 10
                if numerator in old:
                    index = old.index(numerator)
                    a = ans[index:]
                    ans = ans[:index]
                    b = '(' + a + ')'
                    ans += b
                    return ans
                old.append(numerator)
            else:
                numerator *= 10
                old.append(numerator)

a = Solution()
a.fractionToDecimal(1,6)



