# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 递归回溯
class Solution(object):
    def __init__(self):
        self.ans = []
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        temp = []
        self.help(temp, candidates, target)
        return sorted(self.ans)
    def help(self, temp, candidates, target):
        if target<0:
            return
        if target == 0:
            z = sorted(temp[:])
            if z not in self.ans:
                self.ans.append(z)
            return
        for _ in candidates:
            temp.append(_)
            self.help(temp, candidates, target-_)
            del temp[-1]