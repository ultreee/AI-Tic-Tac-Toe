class gameLogic():
    def __init__(self, game):
        self.game = game
        
    # 获胜条件
    def check_win(self, player, new_board=None):
        if new_board is None:
            board = self.game.board
        else:
            board = new_board
        win_conditions = [
            [board[0][0], board[0][1], board[0][2]],
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],
            [board[2][0], board[1][1], board[0][2]]
        ]
        return [player, player, player] in win_conditions
    
    # 是否下满
    def is_board_full(self):
        for row in self.game.board:
            if '' in row:
                return False
        return True

    # 是否允许落子
    def is_legal_place(self, row, col):
        if self.game.board[row][col] != '':
            return False
        return True

    # 清空棋盘
    def clear_board(self):
        for row in range(3):
            for col in range(3):
                self.game.board[row][col] = ''
        self.game.allow_to_play = True
                
    # 切换棋手
    def change_player(self):
        if self.game.current_player == 'X':
            self.game.current_player = 'O'
        elif self.game.current_player == 'O':
            self.game.current_player = 'X'
        
    # 游戏结果
    def check_game_outcome(self, need_change=False):
        # 玩家落子逻辑中判断输赢需要将current_player转换为AI，以表示AI的胜负判断
        if need_change:
            self.change_player()    
        if self.game.game_logic.check_win(self.game.player_pawn):
            self.game.result = "win"
            self.game.current_player = 'X'
            # 记录
            if self.game.player_pawn == 'X':
                self.game.x_score += 1
            elif self.game.player_pawn == 'O':
                self.game.o_score += 1
            return "Done"
        elif self.check_win(self.game.current_player):
            self.game.result = "lose"
            self.game.current_player = 'X'
            # 记录
            if self.game.player_pawn == 'X':
                self.game.o_score += 1
            elif self.game.player_pawn == 'O':
                self.game.x_score += 1
            return "Done"
        if need_change:
            self.change_player()    #撤销
        if self.is_board_full():
            self.game.result = "tie"
            return "Done"
            