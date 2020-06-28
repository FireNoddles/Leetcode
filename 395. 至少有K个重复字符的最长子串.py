# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
#
# 示例 1:
#
# 输入:
# s = "aaabb", k = 3
#
# 输出:
# 3
#
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#分治递归法
# 分治法 如果某个字符在s中出现次数少于k,
# 就不用考虑这个字符了, 因此以这个字符分割然后递归
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if s=='':
            return 0
        for char in set(s):
            if s.count(char)<k:
                partion = s.split(char)
                temp = []
                for _ in partion:
                    temp.append(self.longestSubstring(_,k))
                return max(temp)
        return len(s)
