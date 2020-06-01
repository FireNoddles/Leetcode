# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#示例 2:

# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false

#栈
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sta = []
        for _ in s:
            if _ == '(' or _ == '[' or _ == '{':
                sta.append(_)
            else:
                if len(sta) == 0:
                    return False
                temp = sta.pop()
                if temp == '(' and _!=')':
                    return False
                elif temp == '{' and _!='}':
                    return False
                elif temp == '[' and _!=']':
                    return False
        if len(sta) != 0:
            return False
        else:
            return True