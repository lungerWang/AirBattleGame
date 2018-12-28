
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 创建精灵
        self.__create_sprites()
        # 设置定时器事件-创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)

    def start_game(self):
        print("开始游戏")
        while True:
            # 1.设置游戏帧率
            self.clock.tick(FRAME)
            # 2.设置事件监听
            self.handle_event()
            # 3.碰撞检测
            self.collide_detect()
            # 4.更新绘制精灵
            self.update_sprites()
            # 5.刷新屏幕
            pygame.display.update()
            pass

    def __create_sprites(self):
        bg1 = BackGround()
        bg2 = BackGround(True)
        bg2.rect.y = -bg2.rect.height
        # 背景精灵组
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 敌人飞机精灵组
        self.enemy_group = pygame.sprite.Group()
        pass

    def handle_event(self):
        for event in pygame.event.get():
            # 判断是否点击退出
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌人出现。。。")
                enemy = Enemy()
                self.enemy_group.add(enemy)

    def collide_detect(self):
        pass

    def update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
