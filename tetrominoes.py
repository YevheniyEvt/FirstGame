import pygame
import random
import os

SIZE = 60

O_TETROMINO_IMG = []
I_TETROMINO_IMG = []
L_TETROMINO_IMG = []
J_TETROMINO_IMG = []
S_TETROMINO_IMG = []
T_TETROMINO_IMG = []



class Tetromino:
    color = (163, 181, 49)
    size = SIZE


class Otetromino(Tetromino):
    square_O_tetromino =[]

    def __init__(self):
        self.o_img = O_TETROMINO_IMG
        self.start_x = self.size * 10
        self.start_y = self.size


    def draw_Otetromino(self, window):

        for i in range(2):
            rect = (self.start_x + i*self.size, self.start_y, self.size, self.size)
            self.square_O_tetromino.append(rect)
        for i in range(2):
            rect = (self.start_x + i*self.size, self.start_y + self.size, self.size, self.size)
            self.square_O_tetromino.append(rect)

        for rectangle in self.square_O_tetromino:
            pygame.draw.rect(window, self.color, rectangle,)
            self.square_O_tetromino = self.square_O_tetromino[:4]

class Itetromino(Tetromino):

    def __init__(self):
        self.i_images = random.choice(I_TETROMINO_IMG)

class Ltetromino(Tetromino):

    def __init__(self):
        self.l_images = random.choice(L_TETROMINO_IMG)

class Jtetromino(Tetromino):

    def __init__(self):
        self.j_images = random.choice(J_TETROMINO_IMG)

class Stetromino(Tetromino):

    def __init__(self):
        self.s_images = random.choice(S_TETROMINO_IMG)

class Ttetromino(Tetromino):

    def __init__(self):
        self.t_images = random.choice(T_TETROMINO_IMG)

