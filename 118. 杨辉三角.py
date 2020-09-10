# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        ans = [[1],[1,1]]
        if numRows == 2:
            return ans
        elif numRows == 1:
            return ans[0:1]
        for _ in range(1, numRows-1):
            i = 0
            j = 1
            temp=[1]
            while j != len(ans[_]):
                temp.append(ans[_][i]+ans[_][j])
                i+=1
                j+=1
            temp.append(1)
            ans.append(temp)
        return ans