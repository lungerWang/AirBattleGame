import random
import pygame


SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵"""

    def __init__(self, image_path, speed=1):
        """
        初始化
        :param image_path: 精灵图像
        :param speed: 速度
        """
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 飞行轨迹
        self.rect.y += self.speed


class BackGround(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        """背景精灵"""
        # 如果完全离开屏幕，刷新位置到屏幕顶部
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
        else:
            self.rect.y += self.speed


class Enemy(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(2, 3)
        self.rect.bottom = 0
        # 设置敌人飞机水平方向出现的位置范围
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机挂了。。%s" % self.rect)