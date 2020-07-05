# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]
# 示例 2:
#
# 输入: 5
# 输出: [0,1,1,2,1,2]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/counting-bits
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


import math
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num==0:
            return [0]

        dp = [0 for i in range(num+1)]
        dp[1] = 1
        for _ in range(2, num+1):
            p = int(math.log(_,2))
            c = _ - (2**p)
            if c == 0:
                dp[_]= 1
            else:
                dp[_] = dp[c] + 1
        return dp