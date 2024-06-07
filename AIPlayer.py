class AIPlayer:
    def __init__(self, game):
        self.game = game

    # -------------------------------------------------------------------------------------------------------
    # 迭代加深搜索(简单难度)
    def iterative_deepening_search(self, player, max_depth):
        best_move = None
        for depth in range(1, max_depth + 1):
            best_move = self.depth_limited_search(player, depth)
            if best_move:
                break
        return best_move

    # 深度限制搜索
    def depth_limited_search(self, player, depth):
        if depth == 0 or self.game.game_logic.check_win(self.game.current_player) \
        or self.game.game_logic.check_win(self.game.player_pawn) or self.game.game_logic.is_board_full():
            return None

        possible_moves = self.get_possible_moves()
        for move in possible_moves:
            new_board = self.play_move(move)
            if self.game.game_logic.check_win(player, new_board):
                return move
            
            opponent = self.game.player_pawn if player == self.game.current_player else self.game.player_pawn
            if not self.depth_limited_search(opponent, depth - 1):
                return move
            
        if depth > 1:
            return None
        else:
            if possible_moves:
                return possible_moves[0]
            else:
                return None
        
    # 可以下的位置
    def get_possible_moves(self):
        return [(row, col) for row in range(3) for col in range(3) if self.game.board[row][col] == '']

    # 临时棋盘以便于演算
    def play_move(self, move):
        new_board = [row[:] for row in self.game.board]
        new_board[move[0]][move[1]] = self.game.current_player
        return new_board
    # -------------------------------------------------------------------------------------------------------

    # 极大化极小（普通难度）
    def minimax(self, is_maximizing):
        if self.game.game_logic.check_win(self.game.current_player):
            return 10, None
        elif self.game.game_logic.check_win(self.game.player_pawn):
            return -10, None
        elif self.game.game_logic.is_board_full():
            return 0, None
        
        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.game.board[i][j] == '':
                        self.game.board[i][j] = self.game.current_player
                        score, _ = self.minimax(False)
                        self.game.board[i][j] = ''
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.game.board[i][j] == '':
                        self.game.board[i][j] = self.game.player_pawn
                        score, _ = self.minimax(True)
                        self.game.board[i][j] = ''
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)
            return best_score, best_move
        
    # 极大化极小【剪枝法优化】(困难难度)
    def minimax_with_ab_pruning(self, is_maximizing, alpha=float('-inf'), beta=float('inf')):
        if self.game.game_logic.check_win(self.game.current_player):
            return 10, None
        elif self.game.game_logic.check_win(self.game.player_pawn):
            return -10, None
        elif self.game.game_logic.is_board_full():
            return 0, None
        
        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.game.board[i][j] == '':
                        self.game.board[i][j] = self.game.current_player
                        score, _ = self.minimax_with_ab_pruning(False, alpha, beta)
                        self.game.board[i][j] = ''
                        if score > best_score:
                            best_score = score
                            best_move = (i, j)
                        alpha = max(alpha, score)
                        if beta <= alpha:
                            break
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    if self.game.board[i][j] == '':
                        self.game.board[i][j] = self.game.player_pawn
                        score, _ = self.minimax_with_ab_pruning(True, alpha, beta)
                        self.game.board[i][j] = ''
                        if score < best_score:
                            best_score = score
                            best_move = (i, j)
                        beta = min(beta, score)
                        if beta <= alpha:
                            break
            return best_score, best_move
    
    # AI落子
    def computer_move(self):
        # 简单
        if self.game.difficulty == 'easy':
            move = self.iterative_deepening_search(self.game.current_player, max_depth=9)
            if move:
                self.game.board[move[0]][move[1]] = self.game.current_player
        # 普通
        elif self.game.difficulty == 'normal':
            _, move = self.minimax(True)
            if move:
                self.game.board[move[0]][move[1]] = self.game.current_player
        # 困难
        elif self.game.difficulty == 'hard':
            _, move = self.minimax_with_ab_pruning(True)
            if move:
                self.game.board[move[0]][move[1]] = self.game.current_player
