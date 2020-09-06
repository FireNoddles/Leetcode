# # 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        temp = []
        for i in range(len(num2)-1,-1,-1):
            t = 0
            index = 0
            for j in range(len(num1)-1,-1,-1):
                t += int(num2[i])*int(num1[j]) * (10 **index)
                index+=1
            temp.append(t)
        index = 0
        ans = 0
        for i in temp:
            ans+=i*(10**index)
            index+=1

        return str(ans)