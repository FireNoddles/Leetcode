# 双指针 一个负责走并与下一位比较 一个负责计数
# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
#
# 注意：整数序列中的每一项将表示为一个字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/count-and-say
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = '1'
        for _ in range(1,n):
            temp = ''
            i = 0
            j = 1
            while i<len(s):
                if i == len(s)-1:
                    temp = temp + str(j) + str(s[i])
                    break
                if s[i] != s[i+1]:
                    temp = temp + str(j) + str(s[i])
                    j = 1
                    i+=1
                else:
                    i+=1
                    j+=1
            s = temp
        return s
a =  Solution()
print(a.countAndSay(4))