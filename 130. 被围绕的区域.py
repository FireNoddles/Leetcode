# 给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
#
# 找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
#
# 示例:
#
# X X X X
# X O O X
# X X O X
# X O X X
# 运行你的函数后，矩阵变为：
#
# X X X X
# X X X X
# X X X X
# X O X X
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/surrounded-regions
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#先对边界进行广度遍历 碰到O做标记
#之后再次遍历 O变成X 标记变成O
class Solution(object):
    def __init__(self):
        self.board = []
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board[:]
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                if (i == 0 or i == len(self.board) - 1 or j == 0 or j == len(self.board[0]) - 1) and self.board[i][j] == "O":
                    self.help(i, j)
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                if self.board[i][j] == "O":
                    self.board[i][j] = 'X'
                if self.board[i][j] == "?":
                    self.board[i][j] = 'O'

    def help(self, i, j):
        if i < 0 or j > len(self.board[0]) - 1 or j < 0 or i > len(self.board) - 1:
            return
        if self.board[i][j] == "X" or self.board[i][j] == "?":
            return
        self.board[i][j] = "?"
        self.help(i + 1, j)
        self.help(i - 1, j)
        self.help(i, j + 1)
        self.help(i, j - 1)
a  = Solution()
print(a.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
