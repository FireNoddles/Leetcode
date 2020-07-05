# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。
#
# 注意：
# 总人数少于1100人。
#
# 示例
#
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 排序 先按身高从大到小排序，身高相同按索引从小到大排序
# 之后按照每个人的索引进行插入即可
# On^2
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        people = sorted(people, key=lambda x: (x[0], -x[1]), reverse=True)
        for i in people:
            ans.insert(i[1], i)

        return ans