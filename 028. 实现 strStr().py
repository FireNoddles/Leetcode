# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-strstr
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle =='':
            return 0
        for _ in range(len(haystack)):
            if haystack[_] == needle[0]:
                if _+len(needle) > len(haystack):
                    return -1
                temp = haystack[_:_+len(needle)]
                if temp == needle:
                    return _
        return -1