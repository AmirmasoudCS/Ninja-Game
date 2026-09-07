import pygame
import sys

class Game:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img.set_colorkey((0, 0, 0))
        self.img_pos = [160, 260]
        self.movement = [False, False]
        self.collision_area = pygame.Rect(50, 50, 300, 50)

    def run(self):

        while True:
            self.screen.fill((14, 219, 248))
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5

            self.screen.blit(self.img, self.img_pos)

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height()) # pygame.Rect(*self.img_pos, *self.img.get_size())
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.movement[0] = True
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.movement[0] = False
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.movement[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()