import pygame
from plane_sprites import *

pygame.init()

# 创建英雄矩形
hero_rect = pygame.Rect(200, 600, 102, 126)
print("英雄的xy坐标 (%d, %d)" % (hero_rect.x, hero_rect.y))
print("英雄的宽高 %d*%d" % (hero_rect.width, hero_rect.height))
print("英雄的size %d*%d" % hero_rect.size)

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 加载游戏背景图
bg = pygame.image.load("./images/background.png")
# 绘制游戏背景图
# screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
# screen.blit(hero, (200, 400))

# 刷新游戏窗口
# pygame.display.update()

# 创建精灵和精灵组
enemy = GameSprite("./images/enemy1.png")
sprite_group = pygame.sprite.Group(enemy)

# 游戏时钟对象
clock = pygame.time.Clock()

# 游戏循环
while True:
    clock.tick(60)
    # 获取用户事件并打印
    event_list = pygame.event.get()
    for event in event_list:
        # 实现关闭游戏功能
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    hero_rect.y -= 1
    if hero_rect.y <= -126:
        hero_rect.y = 700
        
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 精灵组绘制和移动
    sprite_group.draw(screen)
    sprite_group.update()

    pygame.display.update()
    pass

pygame.quit()
