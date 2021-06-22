# Author: Roey Mevorach
# June 21, 2021
# Pong Game Player

import pygame

white = (255, 255, 255)

class Ball:
    def __init__(self, speed_x):
        self.x = 310
        self.y = 200
        self.w = 10
        self.h = 10
        self.speed_x = speed_x
        self.speed_y = -2
        self.rect = pygame.rect.Rect((self.x, self.y, self.w, self.h))

    def move(self, col_flag):
        if self.y >= 390 or self.y <= 0:
            self.speed_y = -self.speed_y
        if col_flag:
            self.speed_x = -self.speed_x

        self.rect.move_ip(self.speed_x, self.speed_y)
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, surf):
        pygame.draw.rect(surf, white, self.rect)