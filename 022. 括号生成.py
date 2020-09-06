# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#  
#
# 示例：
#
# 输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#

class Solution(object):
    def __init__(self):
        self.ans = []

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        t = '('
        self.help(t, n)
        return self.ans

    def help(self, temp, n):
        if len(temp) == n * 2:
            self.ans.append(temp)
            return

        if temp.count('(') < n:
            self.help(temp + '(', n)
        if temp.count('(') > temp.count(')'):
            self.help(temp + ')', n)