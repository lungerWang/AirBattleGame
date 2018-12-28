
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()
        self.__create_sprites()

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
        pass

    def handle_event(self):
        for event in pygame.event.get():
            # 判断是否点击退出
            if event.type == pygame.QUIT:
                self.__game_over()

        pass

    def collide_detect(self):
        pass

    def update_sprites(self):
        pass

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
