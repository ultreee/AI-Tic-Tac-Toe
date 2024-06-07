# pawnsSelectionPage.py
import pygame

class pawnsSelectionPage:
    def __init__(self, game):
        self.game = game
        # 加载棋子选择页面的图片
        self.explanation_img = pygame.image.load('./src/images/selection/pawns_selection/choose.png')  # 说明图
        self.x_pawn = pygame.image.load('./src/images/pawns/x_pawn.png')  # X棋子
        self.o_pawn = pygame.image.load('./src/images/pawns/o_pawn.png')  # O棋子
        self.back_button = pygame.image.load('./src/images/round_btn/backward.png')  # 加载返回按钮

        # 设置棋子和说明图的rect
        self.x_pawn_rect = self.x_pawn.get_rect(center=(self.game.screen_size[0]//2 - 90, self.game.screen_size[1]//2 + 100))
        self.o_pawn_rect = self.o_pawn.get_rect(center=(self.game.screen_size[0]//2 + 90, self.game.screen_size[1]//2 + 100))
        self.explanation_img_rect = self.explanation_img.get_rect(center=(self.game.screen_size[0]//2, 200))
        self.back_button_rect = self.back_button.get_rect(topleft=(40, 40))  

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.x_pawn_rect.collidepoint(mouse_pos):
                    # 玩家选择了X棋子
                    self.game.current_page = 'chessboard'
                    self.game.player_pawn = 'X'
                elif self.o_pawn_rect.collidepoint(mouse_pos):
                    # 玩家选择了O棋子
                    self.game.current_page = 'chessboard'
                    self.game.player_pawn = 'O'
                elif self.back_button_rect.collidepoint(mouse_pos):
                    self.game.current_page = 'level_selection'

    def render(self, surface):
        surface.blit(self.explanation_img, self.explanation_img_rect)
        surface.blit(self.x_pawn, self.x_pawn_rect)
        surface.blit(self.o_pawn, self.o_pawn_rect)
        surface.blit(self.back_button, self.back_button_rect) 
