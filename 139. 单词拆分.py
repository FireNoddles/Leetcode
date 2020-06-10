# 递归回溯 暴力 超时
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        temp = ''
        for _ in range(len(s)):
            temp += s[_]
            if temp in wordDict:
                a = self.help(s[_+1:], wordDict)
                if a:
                    return True
        return False

    def help(self, s, wordDict):
        if len(s) == 0:
            return True
        temp = ''
        for _ in range(len(s)):
            temp += s[_]
            if temp in wordDict:
                a = self.help(s[_+1:], wordDict)
                if a:
                    return True
        return False

#动态规划
# 我们可以通过每个word与“s”是不是匹配。我们定义一个布尔dp数组，长度为s.length + 1。
# dp[i]表示字符串s的前i个字符能否拆分成wordDict。我们将每次的都记录下来。
#On^2

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        flag = [False for i in range(len(s)+1)]
        flag[0] = True
        for _ in range(1,len(s)+1):
            for __ in range(0,_):
                if flag[__] == True and s[__:_] in wordDict:
                    flag[_] = True
        return flag[len(s)]