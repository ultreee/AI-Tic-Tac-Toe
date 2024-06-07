# homePage.py
import pygame
import sys

class homePage:
    def __init__(self, game):
        self.game = game
        self.start_button = pygame.image.load('./src/images/round_btn/start.png')
        self.exit_button = pygame.image.load('./src/images/round_btn/exit.png')
        self.tic_tac_toe_logo = pygame.image.load('./src/images/logo/logo.png')

        self.start_button_rect = self.start_button.get_rect(center=(self.game.screen_size[0]//2 - self.start_button.get_width()//2 - 10, self.game.screen_size[1] - 120))
        self.exit_button_rect = self.exit_button.get_rect(center=(self.game.screen_size[0]//2 + self.exit_button.get_width()//2 + 10, self.game.screen_size[1] - 120))
        self.tic_tac_toe_logo_rect = self.tic_tac_toe_logo.get_rect(center=(self.game.screen_size[0]//2, 110))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.start_button_rect.collidepoint(mouse_pos):
                    self.game.current_page = 'level_selection'
                elif self.exit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

    def render(self, surface):
        surface.blit(self.start_button, self.start_button_rect)
        surface.blit(self.exit_button, self.exit_button_rect)
        surface.blit(self.tic_tac_toe_logo, self.tic_tac_toe_logo_rect)
