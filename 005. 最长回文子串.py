#依然从回文串的定义展开讨论：

# 如果一个字符串的头尾两个字符都不相等，那么这个字符串一定不是回文串；
# 如果一个字符串的头尾两个字符相等，才有必要继续判断下去。
# 如果里面的子串是回文，整体就是回文串；
# 如果里面的子串不是回文串，整体就不是回文串。
# 即：在头尾字符相等的情况下，里面子串的回文性质据定了整个子串的回文性质，这就是状态转移。因此可以把「状态」定义为原字符串的一个子串是否为回文子串。
#
# 第 1 步：定义状态
# dp[i][j] 表示子串 s[i..j] 是否为回文子串，这里子串 s[i..j] 定义为左闭右闭区间，可以取到 s[i] 和 s[j]。
#
# 第 2 步：思考状态转移方程
# 在这一步分类讨论（根据头尾字符是否相等），根据上面的分析得到：
#
# dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
# 说明：
#
# 「动态规划」事实上是在填一张二维表格，由于构成子串，因此 i 和 j 的关系是 i <= j ，因此，只需要填这张表格对角线以上的部分。
#
# 看到 dp[i + 1][j - 1] 就得考虑边界情况。
#
# 边界条件是：表达式 [i + 1, j - 1] 不构成区间，即长度严格小于 2，即 j - 1 - (i + 1) + 1 < 2 ，整理得 j - i < 3。
#
# 这个结论很显然：j - i < 3 等价于 j - i + 1 < 4，即当子串 s[i..j] 的长度等于 2 或者等于 3 的时候，其实只需要判断一下头尾两个字符是否相等就可以直接下结论了。
#
# 如果子串 s[i + 1..j - 1] 只有 1 个字符，即去掉两头，剩下中间部分只有 11 个字符，显然是回文；
# 如果子串 s[i + 1..j - 1] 为空串，那么子串 s[i, j] 一定是回文子串。
# 因此，在 s[i] == s[j] 成立和 j - i < 3 的前提下，直接可以下结论，dp[i][j] = true，否则才执行状态转移。
#
# 第 3 步：考虑初始化
# 初始化的时候，单个字符一定是回文串，因此把对角线先初始化为 true，即 dp[i][i] = true 。
#
# 事实上，初始化的部分都可以省去。因为只有一个字符的时候一定是回文，dp[i][i] 根本不会被其它状态值所参考。
#
# 第 4 步：考虑输出
# 只要一得到 dp[i][j] = true，就记录子串的长度和起始位置，没有必要截取，这是因为截取字符串也要消耗性能，记录此时的回文子串的「起始位置」和「回文长度」即可。
#
# 第 5 步：考虑优化空间
# 因为在填表的过程中，只参考了左下方的数值。事实上可以优化，但是增加了代码编写和理解的难度，丢失可读和可解释性。在这里不优化空间。
#
# 注意事项：总是先得到小子串的回文判定，然后大子串才能参考小子串的判断结果，即填表顺序很重要。
#
# 大家能够可以自己动手，画一下表格，相信会对「动态规划」作为一种「表格法」有一个更好的理解。
#
# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#1.动态规划 on^2 on^2
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 1
        st = 0
        flag = [[False for _ in range(len(s))] for _ in range(len(s))]
        for _ in range(len(s)):
            flag[_][_] = True
        for j in range(1,len(s)):
            for i in range(0, j):
                if s[j] == s[i]:
                    if j - i < 3:
                        flag[i][j] = True
                    else:
                        flag[i][j] = flag[i+1][j-1]
                else:
                    flag[i][j] = False
                if flag[i][j]:
                    if maxlen < (j - i + 1):
                        st = i
                        maxlen = j-i + 1
        return s[st: st+ maxlen]

#2. 中心扩散  o^2 o[1]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        st = ''
        if len(s)<2:
            return s
        for i in range(len(s)):
            len_odd = self.help(s,i,i)
            len_even = self.help(s,i,i+1)
            if len(len_odd) > len(len_even) and len(len_odd) > maxlen:
                st = len_odd
                maxlen = len(len_odd)
            if len(len_even) > len(len_odd) and len(len_even) > maxlen:
                st = len_even
                maxlen = len(len_even)
        return st


    def help(self, s, i, j):
        while i >= 0 and j <len(s) and s[i] == s[j]:
            i-=1
            j+=1
        return s[i+1:j]
a = Solution()
print(a.longestPalindrome('babad'))