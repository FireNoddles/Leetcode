# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

class Solution(object):
    def __init__(self):
        self.ans = []
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '' or '1' in digits:
            return []
        dic = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        self.help(digits,0, '',dic)
        return self.ans
    def help(self,digits,index,temp,dic):
        temp = temp[:]
        if digits[index] in dic:
            s = dic[digits[index]]
        else:
            return
        for _ in s:
            if index ==len(digits)-1:
                self.ans.append(temp+_)
            else:
                self.help(digits,index+1,temp+_,dic)

a = Solution()
print(a.letterCombinations('23'))