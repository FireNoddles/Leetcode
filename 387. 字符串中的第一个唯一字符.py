# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#
#  
#
# 示例：
#
# s = "leetcode"
# 返回 0
#
# s = "loveleetcode"
# 返回 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.OrderedDict()
        for _ in s:
            if _ not in dic:
                dic[_] = 1
            else:
                dic[_]+=1
        for _ in dic:
            if dic[_]==1:
                return s.index(_)
        return -1