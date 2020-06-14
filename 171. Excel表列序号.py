# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
# 例如，
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
# 示例 1:
#
# 输入: "A"
# 输出: 1
# 示例 2:
#
# 输入: "AB"
# 输出: 28
# 示例 3:
#
# 输入: "ZY"
# 输出: 701
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/excel-sheet-column-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 每个位置26
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = '0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = 0
        i = 0
        for _ in range(len(s)-1, -1, -1):
            index = dic.index(s[_])
            ans += ((index*(26**i)))
            i+=1
        return ans
