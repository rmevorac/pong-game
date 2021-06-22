# Author: Roey Mevorach
# June 20, 2021
# Pong Game Player

import pygame

white = (255, 255, 255)

class Player:
    def __init__(self, x, y, kind):
        self.score = 0
        self.w = 10
        self.h = 70
        self.x = x
        self.y = y
        self.type = kind
        self.rect = pygame.rect.Rect((self.x, self.y, self.w, self.h))

    def move(self):
        key = pygame.key.get_pressed()

        if self.type == "user1":
            if key[pygame.K_UP] and self.y > 0:
                self.rect.move_ip(0, -3)
                self.y -= 3
            elif key[pygame.K_DOWN] and self.y < 400 - self.h:
                self.rect.move_ip(0, 3)
                self.y += 3
        elif self.type == "user2":
            if key[pygame.K_w] and self.y > 0:
                self.rect.move_ip(0, -3)
                self.y -= 3
            elif key[pygame.K_s] and self.y < 400 - self.h:
                self.rect.move_ip(0, 3)
                self.y += 3
        # elif self.type == "cpu":

    def draw(self, surf):
        pygame.draw.rect(surf, white, self.rect)
