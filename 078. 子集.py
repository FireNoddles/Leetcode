# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 每遍历到一个数字 就把它和当前已有的排列加到一起 变成新排列 On*2^n
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        for _ in nums:
            ans.append([_])
            t = []
            for __ in ans:
                temp = __[:]
                if temp != [_]:
                    temp.append(_)
                    t.append(temp)
            ans.extend(t)
        ans.insert(0,[])
        return ans
a = Solution()
a.subsets([1,2,3])