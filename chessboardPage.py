# chessboardPage.py
import pygame

class chessboardPage:
    def __init__(self, game):
        self.game = game
        self.easy_image = pygame.image.load('./src/images/selection/difficulty_selection/easy_image.png')  # 举例使用easy难度的图片
        self.normal_image = pygame.image.load('./src/images/selection/difficulty_selection/normal_image.png')  # 举例使用easy难度的图片
        self.hard_image = pygame.image.load('./src/images/selection/difficulty_selection/hard_image.png')  # 举例使用easy难度的图片
        self.back_button = pygame.image.load('./src/images/round_btn/backward.png')
        self.replay_button = pygame.image.load('./src/images/round_btn/replay.png')
        self.chessboard = pygame.image.load('./src/images/chessboard/chessboard.png')
        self.scoreboard = pygame.image.load('./src/images/scoreboard/scoreboard.png')
        self.o_pawn = pygame.image.load('./src/images/pawns/o_pawn.png')
        self.x_pawn = pygame.image.load('./src/images/pawns/x_pawn.png')
        self.o_score_img = pygame.image.load('./src/images/pawns/O_scoreImg.png')
        self.x_score_img = pygame.image.load('./src/images/pawns/X_scoreImg.png')
        self.win_image = pygame.image.load('./src/images/match_result/win.png')
        self.lose_image = pygame.image.load('./src/images/match_result/lose.png')
        self.tie_image = pygame.image.load('./src/images/match_result/tie.png')

        # 定位元素
        self.easy_image_rect = self.easy_image.get_rect(center=(self.game.screen_size[0]//2, 75))
        self.normal_image_rect = self.normal_image.get_rect(center=(self.game.screen_size[0]//2, 75))
        self.hard_image_rect = self.hard_image.get_rect(center=(self.game.screen_size[0]//2, 75))
        self.back_button_rect = self.back_button.get_rect(topleft=(40, 40))  
        self.replay_button_rect = self.replay_button.get_rect(topright=(self.game.screen_size[0] - 40, 40))
        self.chessboard_rect = self.chessboard.get_rect(center=(self.game.screen_size[0]//2, self.game.screen_size[1]//2))
        self.scoreboard_rect = self.scoreboard.get_rect(center=(self.game.screen_size[0]//2, self.game.screen_size[1] - 80))
        self.win_image_rect = self.win_image.get_rect(center=(self.game.screen_size[0]//2, self.game.screen_size[1]//2))
        self.lose_image_rect = self.lose_image.get_rect(center=(self.game.screen_size[0]//2, self.game.screen_size[1]//2))
        self.tie_image_rect = self.tie_image.get_rect(center=(self.game.screen_size[0]//2, self.game.screen_size[1]//2))
        
        # 初始化时不加载任何难度图像
        self.difficulty_image = None
        self.difficulty_image_rect = None
        
        self.score_font = pygame.font.Font(None, 60)

    def update_difficulty(self, difficulty):
        # 根据选择的难度加载相应的图像
        if self.game.difficulty == 'easy':
            self.difficulty_image = self.easy_image
            self.difficulty_image_rect = self.easy_image_rect
        elif self.game.difficulty == 'normal':
            self.difficulty_image = self.normal_image
            self.difficulty_image_rect = self.normal_image_rect
        elif self.game.difficulty == 'hard':
            self.difficulty_image = self.hard_image
            self.difficulty_image_rect = self.hard_image_rect
        # 更新难度图像的rect

    def handle_events(self, events, surface):
        for event in events:
            
            # 判断是否轮到AI
            if self.game.current_player != self.game.player_pawn and self.game.allow_to_play:
                self.game.AI_player.computer_move()
                if self.game.game_logic.check_game_outcome() != None:
                    # 锁定棋盘
                    self.game.allow_to_play = False
                    # 结果展示
                    self.show_result(surface)
                    return
                self.game.game_logic.change_player()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
                # 返回
                if self.back_button_rect.collidepoint(mouse_pos):
                    self.game.game_logic.clear_board()
                    self.game.current_page = 'pawns_selection'
                    self.game.x_score = 0
                    self.game.o_score = 0
                # 重玩
                elif self.replay_button_rect.collidepoint(mouse_pos):
                    self.game.game_logic.clear_board()
                    self.game.current_player = 'X'
                # 玩家下棋
                elif self.chessboard_rect.collidepoint(mouse_pos) and self.game.allow_to_play:
                    # 真实棋盘更小一些
                    if mouse_pos[0] > (self.chessboard_rect.left + 40) and mouse_pos[0] < (self.chessboard_rect.right - 40) \
                        and mouse_pos[1] > (self.chessboard_rect.top + 40) and mouse_pos[1] < (self.chessboard_rect.bottom - 40):
                        col = (mouse_pos[0] - self.chessboard_rect.left - 40) // 90
                        row = (mouse_pos[1] - self.chessboard_rect.top - 40) // 90
                        if self.game.game_logic.is_legal_place(row, col) is False:
                            return
                        self.game.board[row][col] = self.game.player_pawn
                        self.draw_board(surface)
                        if self.game.game_logic.check_game_outcome(need_change = True) != None:
                            # 锁定棋盘
                            self.game.allow_to_play = False
                            # 结果展示
                            self.show_result(surface)
                            return
                        self.game.game_logic.change_player()
                            
    # 绘制棋盘
    def draw_board(self, surface):
        for row in range(3):
            for col in range(3):
                pos = (self.chessboard_rect.left + col * 91 + 40, self.chessboard_rect.top + row * 89 + 40)
                if self.game.board[row][col] == 'X':
                    surface.blit(self.x_pawn, pos)
                elif self.game.board[row][col] == 'O':
                    surface.blit(self.o_pawn, pos)
                
    # 绘制分数板
    def draw_scoreboard(self, surface):
        x_pos = (self.scoreboard_rect.left + 70, self.scoreboard_rect.centery - 30)
        o_pos = (self.scoreboard_rect.right - 70 - self.o_score_img.get_width(), self.scoreboard_rect.centery - 35)
        surface.blit(self.x_score_img, x_pos)
        surface.blit(self.o_score_img, o_pos)
        
        # 创建文本对象
        score_text = f':{self.game.x_score} vs {self.game.o_score}:'
        text = self.score_font.render(score_text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.scoreboard_rect.center)

        surface.blit(text, text_rect)

    # 绘制        
    def render(self, surface):
        if self.difficulty_image:
            surface.blit(self.difficulty_image, self.difficulty_image_rect)
        surface.blit(self.back_button, self.back_button_rect)
        surface.blit(self.replay_button, self.replay_button_rect)
        surface.blit(self.chessboard, self.chessboard_rect)
        surface.blit(self.scoreboard, self.scoreboard_rect)
        self.draw_board(surface)
        self.draw_scoreboard(surface)
     
    # 结果展示
    def show_result(self, surface):
        # 全部绘制完成后展示结果
        self.draw_board(surface)
        if self.game.result == "win":
            img = self.win_image
            img_rect = self.win_image_rect
        if self.game.result == "lose":
            img = self.lose_image
            img_rect = self.lose_image_rect
        if self.game.result == "tie":
            img = self.tie_image
            img_rect = self.tie_image_rect
            
        surface.blit(img, img_rect)
        pygame.display.flip()
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                    waiting_for_input = False
                    