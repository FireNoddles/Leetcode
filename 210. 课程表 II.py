# 现在你总共有 n 门课需要选，记为 0 到 n-1。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
#
# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
#
# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: [0,1]
# 解释: 总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/course-schedule-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        dic = {}
        for _ in prerequisites:
            if _[0] not in dic:
                dic[_[0]] = _[1:]
            else:
                dic[_[0]].extend(_[1:])
        que = []
        for _ in range(numCourses):
            if _ not in dic:
                que.insert(0, _)
        while que:
            temp = que.pop()
            numCourses -=1
            ans.append(temp)
            for _ in dic:
                if temp in dic[_]:
                    dic[_].remove(temp)
                    if len(dic[_]) == 0:
                        que.insert(0, _)
                        dic[_] = [-1]
        return ans if numCourses==0 else []