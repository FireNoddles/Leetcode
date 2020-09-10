# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-sudoku
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 每次扫描到一个数字 检查对应的行列块字典是否有重复 有则失败
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        stc = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] !=".":
                    stc_num = (i//3)*3+j//3
                    temp = int (board[i][j])
                    if temp not in row[i]:
                        row[i][temp]=1
                    else:return False
                    if temp not in col[j]:
                        col[j][temp]=1
                    else:return False
                    if temp not in stc[stc_num]:
                        stc[stc_num][temp]=1
                    else:return False
        return True