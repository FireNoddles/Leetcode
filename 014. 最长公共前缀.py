class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        re = ''
        flag  = 0
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        for _ in range(len(strs[0])):
            for __ in range(1,len(strs)):
                if _ > len(strs[__])-1 or strs[__][_] != strs[0][_]:
                    flag = 1
                    break
            if flag == 0:
                re += strs[0][_]
            else:
                flag = 0
        return re
a = Solution()
a.longestCommonPrefix(
["aca","cba"])


#、利用python的max()和min()，在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。所以只需要比较最大最小的公共前缀就是整个数组的公共前缀

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1 or strs[0]=='':
            return ""
        si = min(strs)
        sm = max(strs)
        for _ in range(len(si)):
            if si[_] != sm[_]:
                return sm[:_]
        return si