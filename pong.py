# Author: Roey Mevorach
# June 19, 2021
# Pong Game

import sys
import pygame
import time
import player, ball
from pygame.locals import *

black = (0,0,0)
white = (255, 255, 255)
red = (255, 0, 0)

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.clock = pygame.time.Clock()
        self.player1 = player.Player(615, 175, "user1")
        self.player2 = player.Player(25, 175, "user2")
        self.b = ball.Ball(2)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_render(self):
        self._display_surf.fill(black)
        self.player1.draw(self._display_surf)
        self.player2.draw(self._display_surf)
        self.b.draw(self._display_surf)
        self.player1.move()
        self.player2.move()

        self.show_score()
        pygame.display.update()
        self.clock.tick(120)
      
    def on_cleanup(self):
        pygame.quit()

    def score(self):
        if self.b.x > self.width:
            self.player2.score += 1
            self.b = ball.Ball(2)
        elif self.b.x < -10:
            self.player1.score += 1
            self.b = ball.Ball(-2)

    def collisions(self):
        flag = False

        if pygame.Rect.colliderect(self.b.rect, self.player1.rect) or \
         pygame.Rect.colliderect(self.player2.rect, self.b.rect):
            flag = True

        self.b.move(flag)

    def show_score(self):
        largeText = pygame.font.Font('Retro Gaming.ttf', 35)
        score1_text_center = ((self.width/2 + 30),(self.height - 375))
        score1_text_rect = self.draw_text(str(self.player1.score), largeText, white, score1_text_center)
        score2_text_center = ((self.width/2 - 30),(self.height - 375))
        score2_text_rect = self.draw_text(str(self.player2.score), largeText, white, score2_text_center)

    def text_objects(self, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def draw_text(self, msg, font, color, center):
        surf, rect = self.text_objects(msg, font, color)
        rect.center = center
        self._display_surf.blit(surf, rect)
        return rect

    def highlight_text(self, right, left, top, bottom, mouse_pos):
        if left <= mouse_pos[0] <= right \
         and top <= mouse_pos[1] <= bottom:
            return red
        else:
            return white

    def reset_scores(self):
        self.player1.score = 0
        self.player2.score = 0

    def winning(self, msg):
        largeText = pygame.font.Font('Retro Gaming.ttf', 60)
        winning_text_center = ((self.width/2),(self.height/2))
        winning_text_rect = self.draw_text(msg, largeText, white, winning_text_center)
        pygame.display.update()
        pygame.event.set_blocked(None)
        pygame.event.set_allowed(pygame.KEYUP)
        pygame.event.wait()
        pygame.event.set_allowed(None)

    def game_intro(self):
        if self.on_init() == False:
            self._running = False

        intro = True

        while intro:
            for event in pygame.event.get():
                print(event)

                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if player1_text_rect.left <= mouse_x <= player1_text_rect.right \
                     and player1_text_rect.top <= mouse_y <= player1_text_rect.bottom:
                        self.on_execute(1)
                        print("1 player")
                    
                    elif player2_text_rect.left <= mouse_x <= player2_text_rect.right \
                     and player2_text_rect.top <= mouse_y <= player2_text_rect.bottom:
                        self.on_execute(2)
                        print("2 player")

                    elif quit_rect.left <= mouse_x <= quit_rect.right \
                     and quit_rect.top <= mouse_y <= quit_rect.bottom:
                        intro = False
                        pygame.quit()
                        quit()
                        
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self._display_surf.fill(black)
            largeText = pygame.font.Font('Retro Gaming.ttf',25)
            player1_text_center = ((self.width/2),(self.height/2 - 50))
            player2_text_center = ((self.width/2),(self.height/2))
            quit_center = ((self.width/2),(self.height/2 + 50))

            mouse = pygame.mouse.get_pos()
            player1_text_color = self.highlight_text(381, 260, 138, 163, mouse)
            player2_text_color = self.highlight_text(390, 250, 188, 213, mouse)
            quit_color = self.highlight_text(351, 290, 238, 263, mouse)

            player1_text_rect = self.draw_text("1 PLAYER", largeText, player1_text_color, player1_text_center)
            player2_text_rect = self.draw_text("2 PLAYERS", largeText, player2_text_color, player2_text_center)
            quit_rect = self.draw_text("QUIT", largeText, quit_color, quit_center)

            pygame.display.update()
 
    def on_execute(self, num_players):
        self._display_surf.fill(black)
        if num_players == 1:
            self.player2.type = "cpu"
        else:
            self.player2.type = "user2"

        self.player1.score = 0
        self.player2.score = 0

        while(self._running):
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.score()

            if self.player1.score == 3:
                self.winning("PLAYER 1 WINS")
                return
            elif self.player2.score == 3:
                self.winning("PLAYER 2 WINS")
                return

            self.collisions()
            self.on_render()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.game_intro()