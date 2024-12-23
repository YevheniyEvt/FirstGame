import pygame
import random
import os

SIZE = 60
SCALE =10
WIDTH, HEIGHT = SIZE*SCALE*1.29, SIZE*SCALE*1.05

GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT = WIDTH - (SIZE * (WIDTH/SIZE)*0.3), HEIGHT*0.999
PRE_GAME_WIDTH, PRE_GAME_HEIGHT = WIDTH-GAME_FIELD_WIDTH, HEIGHT*0.4
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

class Tetromino:
    color = (163, 181, 49)
    size = SIZE*0.97
    start_x = int(size*SCALE)
    start_y = int(size)
    square_tetromino = []


class Otetromino(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(2):
            rect = (self.start_x + i*self.size+self.size*0.4, self.start_y, self.size, self.size)
            self.square_tetromino.append(rect)
        for i in range(2):
            rect = (self.start_x + i*self.size+self.size*0.4, self.start_y + self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]


class Itetromino(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x + self.size, self.start_y + i*self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:3]

class ItetrominoTwo(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x+i*self.size, self.start_y+self.size*0.5, self.size, self.size)
            self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:3]


class Ltetromino(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x+i*self.size, self.start_y+self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        rect = (self.start_x, self.start_y+self.size+self.size, self.size, self.size)
        self.square_tetromino.append(rect)

        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class LtetrominoTwo(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x + self.size, self.start_y + i*self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        rect = (self.start_x, self.start_y, self.size, self.size)
        self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]
class Jtetromino(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x + self.size*0.5, self.start_y + i*self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        rect = (self.start_x + self.size*0.5 + self.size, self.start_y, self.size, self.size)
        self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class JtetrominoTwo(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x+i*self.size, self.start_y+self.size*0.5, self.size, self.size)
            self.square_tetromino.append(rect)
        rect = (self.start_x+2*self.size, self.start_y+self.size+self.size*0.5, self.size, self.size)
        self.square_tetromino.append(rect)

        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class JtetrominoThree(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x+i*self.size, self.start_y+self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        rect = (self.start_x, self.start_y, self.size, self.size)
        self.square_tetromino.append(rect)

        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class JtetrominoFour(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x + self.size, self.start_y + i*self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        rect = (self.start_x, self.start_y+self.size*2, self.size, self.size)
        self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class Stetromino(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(2):
            rect = (self.start_x + i*self.size, self.start_y, self.size, self.size)
            self.square_tetromino.append(rect)
        for i in range(2):
            rect = (self.start_x + i*self.size+self.size, self.start_y + self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class StetrominoTwo(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(2):
            rect = (self.start_x + i*self.size+self.size, self.start_y, self.size, self.size)
            self.square_tetromino.append(rect)
        for i in range(2):
            rect = (self.start_x + i*self.size, self.start_y + self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class StetrominoThree(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(2):
            rect = (self.start_x + i*self.size+self.size*0.5, self.start_y+i*self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for i in range(2):
            rect = (self.start_x + i*self.size+self.size*0.5, self.start_y + i*self.size+self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class StetrominoFour(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(2):
            rect = (self.start_x + self.size+self.size*0.5, self.start_y+i*self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for i in range(2):
            rect = (self.start_x +self.size*0.5, self.start_y + i*self.size+self.size, self.size, self.size)
            self.square_tetromino.append(rect)
        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

class Ttetromino(Tetromino):
    square_tetromino = []

    def draw_tetromino(self, window):
        for i in range(3):
            rect = (self.start_x+i*self.size*0.9, self.start_y+self.size*0.5, self.size, self.size)
            self.square_tetromino.append(rect)
        rect = (self.start_x+self.size*0.9, self.start_y+self.size+self.size*0.5, self.size, self.size)
        self.square_tetromino.append(rect)

        for rectangle in self.square_tetromino:
            pygame.draw.rect(window, self.color, rectangle)
            self.square_tetromino = self.square_tetromino[:4]

