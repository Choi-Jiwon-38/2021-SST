import pygame

class Player:
    def __init__(self, width, height):
        self.image = pygame.image.load('player.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.pos = [width, height]
        self.to = [0, 0]
        self.acc = [0, 0]

    def draw(self, screen):
        calib_pos = (self.pos[0] - self.image.get_width()/2, self.image.get_height()/2)
        screen.blit(self.image, self.pos)

    def goto(self, x, y):
        self.to[0] += x
        self.to[1] += y
        print(self.to)

    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + self.to[0] * dt) % width # x좌표
        self.pos[1] = (self.pos[1] + self.to[1] * dt) % height # y좌표