# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        tar = x
        if x <0:
            return False
        if x <10:
            return True
        ans = 0
        while x > 0:
            r = x % 10
            ans *= 10
            ans+=r
            x = x//10
        return True if ans==tar else False