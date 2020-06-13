# 根据逆波兰表示法，求表达式的值。
#
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
#
# 说明：
#
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 示例 1：
#
# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/evaluate-reverse-polish-notation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ans = 0
        for _ in tokens:
            if _ not in '+-*/':
                stack.append(int(_))
            else:
                a = stack.pop()
                b = stack.pop()
                if _ == '+':
                    stack.append(b + a)
                elif _ == '-':
                    stack.append(b - a)
                elif _ == '*':
                    stack.append(b * a)
                else:

                    if a < 0 and b > 0:
                        c = b / (-a)
                        c = - int(c)
                    elif a > 0 and b < 0:
                        c = -b / a
                        c = - int(c)
                    else:
                        c = int(b / a)
                    stack.append(c)
        return stack[-1]

a = Solution()
a.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
