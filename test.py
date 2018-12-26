import pygame

pygame.init()

# 创建英雄矩形
hero_rect = pygame.Rect(500, 600, 50, 60)
print("英雄的xy坐标 (%d, %d)" % (hero_rect.x, hero_rect.y))
print("英雄的宽高 %d*%d" % (hero_rect.width, hero_rect.height))
print("英雄的size %d*%d" % hero_rect.size)

# 创建游戏窗口
screen = pygame.display.set_mode((480, 800))

# 游戏循环
while True:
    pass

pygame.quit()
