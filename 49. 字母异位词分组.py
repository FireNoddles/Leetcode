#给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# 】
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/group-anagrams
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 先哈希 再输出
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for _ in strs:
            temp = str(sorted(_))
            if temp not in dic:
                dic[temp] = [_]
            else:
                dic[temp].append(_)
        return list(dic.values())
