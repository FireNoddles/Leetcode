# 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。
#
# 说明: 
#
# 如果题目有解，该答案即为唯一答案。
# 输入数组均为非空数组，且长度相同。
# 输入数组中的元素均为非负数。
# 示例 1:
#
# 输入:
# gas  = [1,2,3,4,5]
# cost = [3,4,5,1,2]
#
# 输出: 3
#
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/gas-station
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 暴力法 On^2
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 1:
            if gas[0] < cost[0]:
                return -1
            else:
                return 0
        for i in range(len(gas)):
            init = gas[i] - cost[i]
            if init>=0:
                temp1 = gas[i:]
                temp1.extend(gas[:i])
                temp2 = cost[i:]
                temp2.extend(cost[:i])
                if self.iscan(init, temp1,temp2):
                    return i
        return -1

    def iscan(self, init, gas, cost):
        for _ in range(1,len(gas)):
            init = init + gas[_] - cost[_]
            if init < 0:
                break
        if _ == len(gas)-1 and init>=0:
            return True
        return False

# 首先 当全部消耗大于全部加油数时 怎么也不会成功 选择一个变量记录所有消耗和加油
# 当最后大于=0时说明有结果 找到遍历时到最后都不为0的点
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if len(gas) == 1:
            if gas[0] < cost[0]:
                return -1
            else:
                return 0
        total = 0
        cur = 0
        index = 0
        for i in range(len(gas)):
            total = total + gas[i] - cost[i]
            cur = cur + gas[i] - cost[i]
            if cur < 0:
                index = i+1
                cur = 0
        return index if total>=0 else -1