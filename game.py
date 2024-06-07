# game.py
import pygame
import sys
from homePage import homePage
from levelSelectionPage import levelSelectionPage
from pawnsSelectionPage import pawnsSelectionPage
from chessboardPage import chessboardPage
from gameLogic import gameLogic
from AIPlayer import AIPlayer

class Game:
    def __init__(self):
        pygame.init()
        self.screen_size = (500, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("井字棋游戏")
        icon = pygame.image.load('./src/images/logo/ticTacToe.png')
        pygame.display.set_icon(icon)

        # 加载和调整底板图片
        self.baseboard = pygame.image.load('./src/images/baseboard/baseboard.png')
        self.baseboard = pygame.transform.scale(self.baseboard, self.screen_size)

        # 页面实例
        self.home_page = homePage(self)
        self.level_selection_page = levelSelectionPage(self)
        self.pawns_selection_page = pawnsSelectionPage(self)
        self.chessboard_page = chessboardPage(self)
        self.game_logic = gameLogic(self)
        self.AI_player = AIPlayer(self)

        self.difficulty = None
        self.player_pawn = None
        self.current_page = 'home'
        self.allow_to_play = True
        self.result = None
        # X先手
        self.current_player = 'X'
        # 定义棋盘
        self.board = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]
        # 分数记录
        self.x_score = 0
        self.o_score = 0

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            # 清屏并绘制底板
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.baseboard, (0, 0))  # 在这里绘制底板图片

            # 根据当前页面状态，调用相应页面的逻辑和渲染函数
            if self.current_page == 'home':
                self.home_page.handle_events(events)
                self.home_page.render(self.screen)
            elif self.current_page == 'level_selection':
                self.level_selection_page.handle_events(events)
                self.level_selection_page.render(self.screen)
            elif self.current_page == 'pawns_selection':
                self.pawns_selection_page.handle_events(events)
                self.pawns_selection_page.render(self.screen)
            elif self.current_page == 'chessboard':
                self.chessboard_page.update_difficulty(self.difficulty)  # 根据选择的难度更新棋盘页面
                
                self.chessboard_page.render(self.screen)
                self.chessboard_page.handle_events(events, self.screen)
                

            pygame.display.flip()

        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()
