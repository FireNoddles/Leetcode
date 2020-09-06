# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/combination-sum-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def __init__(self):
        self.ans = []

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if sum(candidates) < target: return []
        self.help([], candidates, target)
        return sorted(self.ans)

    def help(self, temp, candidates, target):
        t = sorted(temp)
        if sum(t) > target: return
        if sum(t) == target and t not in self.ans:
            self.ans.append(t)
            return
        for i in range(len(candidates)):
            if sum(t) + candidates[i] <= target:
                c = candidates[:]
                t.append(candidates[i])
                del c[i]
                self.help(t, c, target)
                del t[-1]

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        temp = []
        for i in range(len(num2)-1,-1,-1):
            t = 0
            index = 0
            for j in range(len(num1)-1,-1,-1):
                t += (int(num2[i] * int(num1[j]))) * (10 **index)
