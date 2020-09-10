# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        arr = ['' for _ in range(numRows)]
        i = 0
        flag = 0
        while i < len(s):
            if flag == 0:
                for _ in range(0,numRows-1):
                    if i < len(s):
                        arr[_]+=s[i]
                    i+=1
                flag = 1
            if flag==1:
                for __ in range(numRows-1,0,-1):
                    if i < len(s):
                        arr[__]+=s[i]
                    i+=1
                flag = 0
        return ''.join(arr)