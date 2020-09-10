# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/palindrome-partitioning
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 递归回溯
#每一层从字符串的第一位开始判断是否是回文 如果是就传之后的字符串到下一层
class Solution(object):
    def __init__(self):
        self.ans = []
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s)==1:
            return [[s]]
        if len(s)==0:
            return []
        self.help(s, [])
        return self.ans
    def ishuiwen(self, s):
        i = 0
        j = len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def help(self, s, temp_ans):
        temp = temp_ans[:]
        if len(s)==0:
            self.ans.append(temp)
            return
        for _ in range(len(s)):
            if (self.ishuiwen(s[:_+1])):
                temp.append(s[:_+1])
                self.help(s[ _+1:], temp)
                del temp[-1] # 还原

a = Solution()
a.partition('aab')