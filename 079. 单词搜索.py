# #给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#  
#
# 示例:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/word-search
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


#递归回溯
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        flag = [1] * (len(board) * len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    a = self.help(board, word, i, j, flag)
                    if a:
                        return True
        return False

    def help(self, board, word, i, j, flag):
        new_flag = flag[:]
        if board[i][j] != word[0] or new_flag[i * len(board[0]) + j] == 0:
            return False
        else:
            if len(word) == 1:
                return True
            new_flag[i * len(board[0]) + j] = 0
            if i > 0 and self.help(board, word[1:], i - 1, j, new_flag):
                return True
            elif i < len(board) - 1 and self.help(board, word[1:], i + 1, j, new_flag):
                return True
            elif j > 0 and self.help(board, word[1:], i, j - 1, new_flag):
                return True
            elif j < len(board[0]) - 1 and self.help(board, word[1:], i, j + 1, new_flag):
                return True
            return False