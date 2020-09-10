# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        i = 0
        j = len(s)-1
        dic = 'abcdefghijklmnopqrstuvwxyz0123456789'
        while j-i>=1:
            while i <len(s)-1 and s[i] not in dic:
                i+=1
            while j >0 and s[j] not in dic:
                j-=1
            if s[i]!=s[j] and s[i] in dic:
                return False
            else:
                i+=1
                j-=1
        return True
a= Solution()
a.isPalindrome("A man, a plan, a canal: Panama")