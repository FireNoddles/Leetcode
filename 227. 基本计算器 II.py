# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
#
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
#
# 示例 1:
#
# 输入: "3+2*2"
# 输出: 7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/basic-calculator-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#栈 碰到一个数若它之前的符号是加法或减法，入栈 ； 若是乘法或除法 出栈 和当前数运算后放入栈
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        ans , stack, sign = 0, [], '+'
        for _ in range(len(s)):
            if s[_] in '0123456789':
                ans=ans*10+int(s[_])
            if s[_] in '+-*/' or _ == len(s)-1:
                if sign == '+':
                    stack.append(ans)
                elif sign == '-':
                    stack.append(-ans)
                elif sign == '*':
                    stack.append(stack.pop()*ans)
                else:
                    stack.append(int(stack.pop()/ans))
                sign = s[_]
                ans = 0
        return sum(stack)
