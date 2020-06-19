# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-anagram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 哈希
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        arr = []
        for _ in s:
            arr.append(_)
        for _ in t:
            if _ not in arr:
                return False
            else:
                arr.remove(_)
        return True


# 排序
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t) or sorted(s) != sorted(t):
            return False
        return True