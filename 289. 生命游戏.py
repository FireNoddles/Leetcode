# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
#
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
#
#  
#
# 示例：
#
# 输入：
# [
#   [0,1,0],
#   [0,0,1],
#   [1,1,1],
#   [0,0,0]
# ]
# 输出：
# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/game-of-life
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# 暴力 Omn Omn  如果可以将矩阵里面重新定义一个状态（原矩阵只能为1或0）
# 如 可以用2来表示该位置原来是死的 现在是活的
# 就可以直接在原矩阵进行直接修改 节省空间为O1
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        arr = [[0 for i in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp = 0
                if i > 0 and board[i-1][j]==1:
                    temp+=1
                if i>0 and j< len(board[0])-1 and board[i-1][j+1]==1:
                    temp+=1
                if j< len(board[0])-1 and  board[i][j+1]==1:
                    temp+=1
                if i < len(board)-1 and j< len(board[0])-1 and board[i+1][j+1]==1:
                    temp+=1
                if i < len(board)-1 and board[i+1][j]==1:
                    temp+=1
                if i<len(board)-1 and j>0 and board[i+1][j-1]==1:
                    temp+=1
                if j>0 and board[i][j-1]==1:
                    temp+=1
                if i> 0 and j > 0 and board[i-1][j-1] ==1:
                    temp+=1
                if temp <2:
                    arr[i][j] = 0
                elif 2<=temp<=3:
                    if board[i][j]==1:
                        arr[i][j] = 1
                    else:
                        if temp == 3:
                            arr[i][j] = 1
                        else:
                            arr[i][j]=0
                elif temp > 3:
                    arr[i][j] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = arr[i][j]