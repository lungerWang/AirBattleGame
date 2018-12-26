import pygame

pygame.init()

# 创建英雄矩形
hero_rect = pygame.Rect(500, 600, 50, 60)
print("英雄的xy坐标 (%d, %d)" % (hero_rect.x, hero_rect.y))
print("英雄的宽高 %d*%d" % (hero_rect.width, hero_rect.height))
print("英雄的size %d*%d" % hero_rect.size)

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 加载游戏背景图
bg = pygame.image.load("./images/background.png")
# 绘制游戏背景图
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 400))

# 刷新游戏窗口
pygame.display.update()




# 游戏循环
while True:
    pass

pygame.quit()
