# 你这个学期必须选修 numCourse 门课程，记为 0 到 numCourse-1 。
#
# 在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们：[0,1]
#
# 给定课程总量以及它们的先决条件，请你判断是否可能完成所有课程的学习？
#
#  
#
# 示例 1:
#
# 输入: 2, [[1,0]]
# 输出: true
# 解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/course-schedule
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 拓扑排序 借用队列
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        dic = {}
        que = []
        for _ in prerequisites:
            if _[0] not in dic:
                dic[_[0]] = [_[1]]
            else:
                dic[_[0]].append(_[1])
        for _ in range(numCourses):
            if _ not in dic:
                que.insert(0, _)
        while que:
            temp = que.pop()
            # 计数 以判断是否有环
            numCourses -=1
            for _ in dic:
                if temp in dic[_]:
                    dic[_].remove(temp)
                if len(dic[_]) == 0:
                    dic[_] = [-1]
                    que.insert(0, _)
        return numCourses == 0

a = Solution()
a.canFinish(2,
[[1,0]])