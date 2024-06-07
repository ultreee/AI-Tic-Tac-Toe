import pygame
import sys

# 初始化pygame
pygame.init()

# 设置屏幕大小
screen_size = (500, 600)
screen = pygame.display.set_mode(screen_size)

# 设置标题
pygame.display.set_caption("井字棋游戏")

# 加载图像
baseboard = pygame.image.load('./src/images/baseboard/baseboard_1.png')
start_button = pygame.image.load('./src/images/round_btn/start.png')
exit_button = pygame.image.load('./src/images/round_btn/exit.png')
tic_tac_toe_logo = pygame.image.load('./src/images/logo/logo.png')

# 在游戏主循环外部，加载第二页面的按钮图像
easy_button = pygame.image.load('./src/images/selection/difficulty_selection/easy_btn.png')
normal_button = pygame.image.load('./src/images/selection/difficulty_selection/normal_btn.png')
hard_button = pygame.image.load('./src/images/selection/difficulty_selection/hard_btn.png')
back_button = pygame.image.load('./src/images/round_btn/backward.png')  # 返回键

# 创建按钮的rect，用于后续的碰撞检测，根据您提供的数值和设计来定位
easy_button_rect = easy_button.get_rect(center=(screen_size[0]//2, 150))
normal_button_rect = normal_button.get_rect(center=(screen_size[0]//2, 150*2))  # 加上按钮高度和一些间隔
hard_button_rect = hard_button.get_rect(center=(screen_size[0]//2, 150*3))
back_button_rect = back_button.get_rect(topleft=(40, 40))  # 假设放在左上角

# 调整底板图片以适应屏幕尺寸
baseboard = pygame.transform.scale(baseboard, screen_size)

# 计算按钮和logo的摆放位置
start_button_rect = start_button.get_rect(center=(screen_size[0]//2 - start_button.get_width()//2 - 10, screen_size[1] - 120))
exit_button_rect = exit_button.get_rect(center=(screen_size[0]//2 + exit_button.get_width()//2 + 10, screen_size[1] - 120))
tic_tac_toe_logo_rect = tic_tac_toe_logo.get_rect(center=(screen_size[0]//2, 110))

# 游戏状态标识
current_page = 'home'

# 游戏主循环
running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if current_page == 'home':
                # 检查是否点击了开始按钮
                if start_button_rect.collidepoint(mouse_pos):
                    current_page = 'level_selection'
                # 检查是否点击了退出按钮
                elif exit_button_rect.collidepoint(mouse_pos):
                    running = False
            elif current_page == 'level_selection':
                # 检查是否点击了返回按钮
                if back_button_rect.collidepoint(mouse_pos):
                    current_page = 'home'
                # 检查是否点击了简单难度按钮
                elif easy_button_rect.collidepoint(mouse_pos):
                    print("easy")
                # 检查是否点击了普通难度按钮
                elif normal_button_rect.collidepoint(mouse_pos):
                    print("normal")
                # 检查是否点击了困难难度按钮
                elif hard_button_rect.collidepoint(mouse_pos):
                    print("hard")

    # 绘制背景和元素
    screen.fill((0, 0, 0))  # 可以用一个合适的背景色填充屏幕
    
    screen.blit(baseboard, (0, 0))  # 底板图片居中绘制
    if current_page == 'home':
        screen.blit(start_button, start_button_rect)
        screen.blit(exit_button, exit_button_rect)
        screen.blit(tic_tac_toe_logo, tic_tac_toe_logo_rect)
    elif current_page == 'level_selection':
        # 绘制第二页面的元素
        screen.blit(back_button, back_button_rect)
        screen.blit(easy_button, easy_button_rect)
        screen.blit(normal_button, normal_button_rect)
        screen.blit(hard_button, hard_button_rect)

    # 刷新屏幕
    pygame.display.flip()

# 退出pygame
pygame.quit()
sys.exit()