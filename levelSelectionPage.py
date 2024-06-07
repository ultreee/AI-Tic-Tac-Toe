# levelSelectionPage.py
import pygame

class levelSelectionPage:
    def __init__(self, game):
        self.game = game
        self.back_button = pygame.image.load('./src/images/round_btn/backward.png')
        self.easy_button = pygame.image.load('./src/images/selection/difficulty_selection/easy_btn.png')
        self.normal_button = pygame.image.load('./src/images/selection/difficulty_selection/normal_btn.png')
        self.hard_button = pygame.image.load('./src/images/selection/difficulty_selection/hard_btn.png')

        self.back_button_rect = self.back_button.get_rect(topleft=(40, 40))
        self.easy_button_rect = self.easy_button.get_rect(center=(self.game.screen_size[0]//2, 150))
        self.normal_button_rect = self.normal_button.get_rect(center=(self.game.screen_size[0]//2, 150*2))
        self.hard_button_rect = self.hard_button.get_rect(center=(self.game.screen_size[0]//2, 150*3))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.back_button_rect.collidepoint(mouse_pos):
                    self.game.current_page = 'home'
                elif self.easy_button_rect.collidepoint(mouse_pos):
                    self.game.difficulty = 'easy'
                    self.game.current_page = 'pawns_selection'
                elif self.normal_button_rect.collidepoint(mouse_pos):
                    self.game.difficulty = 'normal'
                    self.game.current_page = 'pawns_selection'
                elif self.hard_button_rect.collidepoint(mouse_pos):
                    self.game.difficulty = 'hard'
                    self.game.current_page = 'pawns_selection'

    def render(self, surface):
        surface.blit(self.back_button, self.back_button_rect)
        surface.blit(self.easy_button, self.easy_button_rect)
        surface.blit(self.normal_button, self.normal_button_rect)
        surface.blit(self.hard_button, self.hard_button_rect)
