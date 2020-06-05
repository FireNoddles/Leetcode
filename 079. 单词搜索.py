#


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