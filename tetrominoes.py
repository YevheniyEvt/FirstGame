import pygame


SIZE = 40
SCALE =15
WIDTH, HEIGHT = SIZE*SCALE*1.3, SIZE*SCALE

GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT = WIDTH - (SIZE * (WIDTH/SIZE)*0.3), HEIGHT
PRE_GAME_WIDTH, PRE_GAME_HEIGHT = WIDTH-GAME_FIELD_WIDTH, HEIGHT*0.4
SCORE_FIELD_WIDTH, SCORE_FIELD_HEIGHT = PRE_GAME_WIDTH, GAME_FIELD_HEIGHT - PRE_GAME_HEIGHT

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


class Tetromino:
    _color = (149, 52, 235)
    _size = SIZE * 0.97
    _start_x = int(_size * SCALE)
    _start_y = int(_size)
    _square_tetromino = []
    _index_height = 0
    _index_width = 0

    def set_start_x(self, start_x):
        self._start_x = start_x
    def set_start_y(self, start_y):
        self._start_y = start_y

    def get_start_x(self):
        return self._start_x
    def get_start_y(self):
        return self._start_y

    def set_square(self, rectangles):
        self._square_tetromino = rectangles

    def get_square(self):
        return self._square_tetromino

    def add_rectangle(self, rect):
        self._square_tetromino.append(rect)

    def delete_tetromino(self):
        self._square_tetromino = []

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def get_size(self):
        return self._size

    def get_index_height(self):
        return self._index_height

    def get_index_width(self):
        return self._index_width

    def draw_tetromino(self, window):
        self.create_tetromino()
        for rectangle in self.get_square():
            pygame.draw.rect(window, self.get_color(), rectangle,10,10)


class Otetromino(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_height()):
            rect = (self._start_x + i * self._size + self._size * 0.4, self._start_y, self._size, self._size)
            self.add_rectangle(rect)
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size + self._size * 0.4, self._start_y + self._size, self._size, self._size)
            self.add_rectangle(rect)


class Itetromino(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 1

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_height()):
            rect = (self._start_x, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)


class ItetrominoTwo(Tetromino):
    _square_tetromino = []
    _index_height = 1
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size, self._start_y, self._size, self._size)
            self.add_rectangle(rect)


class Ltetromino(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size, self._start_y, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x, self._start_y + self._size, self._size, self._size)
        self.add_rectangle(rect)


class LtetrominoTwo(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_height()):
            rect = (self._start_x + self._size, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x, self._start_y, self._size, self._size)
        self.add_rectangle(rect)


class LtetrominoThree(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + self._size*i, self._start_y + self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x+self._size*self.get_index_height(), self._start_y, self._size, self._size)
        self.add_rectangle(rect)


class LtetrominoFour(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + self._size*i, self._start_y + self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x, self._start_y+self.get_size()*self.get_index_height(), self._size, self._size)
        self.add_rectangle(rect)


class Jtetromino(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_height()):
            rect = (self._start_x, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x + self._size, self._start_y, self._size, self._size)
        self.add_rectangle(rect)


class JtetrominoTwo(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size, self._start_y, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x + 2 * self._size, self._start_y + self._size, self._size, self._size)
        self.add_rectangle(rect)


class JtetrominoThree(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size, self._start_y + self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x, self._start_y, self._size, self._size)
        self.add_rectangle(rect)


class JtetrominoFour(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_height()):
            rect = (self._start_x + self._size, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x, self._start_y + self._size * self.get_index_width(), self._size, self._size)
        self.add_rectangle(rect)


class Stetromino(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()-1):
            rect = (self._start_x + i * self._size, self._start_y, self._size, self._size)
            self.add_rectangle(rect)
        for i in range(self.get_index_height()):
            rect = (self._start_x + i * self._size + self._size, self._start_y + self._size, self._size, self._size)
            self.add_rectangle(rect)


class StetrominoTwo(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()-1):
            rect = (self._start_x + i * self._size + self._size, self._start_y, self._size, self._size)
            self.add_rectangle(rect)
        for i in range(self.get_index_height()):
            rect = (self._start_x + i * self._size, self._start_y + self._size, self._size, self._size)
            self.add_rectangle(rect)


class StetrominoThree(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)
        for i in range(self.get_index_height()-1):
            rect = (self._start_x + i * self._size, self._start_y + i * self._size + self._size, self._size, self._size)
            self.add_rectangle(rect)


class StetrominoFour(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + self._size, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)
        for i in range(self.get_index_height()-1):
            rect = (self._start_x, self._start_y + i * self._size + self._size, self._size, self._size)
            self.add_rectangle(rect)


class Ttetromino(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size, self._start_y, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x + self._size, self._start_y + self._size, self._size, self._size)
        self.add_rectangle(rect)

class TtetrominoTwo(Tetromino):
    _square_tetromino = []
    _index_height = 2
    _index_width = 3

    def create_tetromino(self):
        self.delete_tetromino()
        rect = (self._start_x + self._size, self._start_y + self._size, self._size, self._size)
        self.add_rectangle(rect)
        for i in range(self.get_index_width()):
            rect = (self._start_x + i * self._size, self._start_y +self.get_size()*self.get_index_height(), self._size, self._size)
            self.add_rectangle(rect)


class TtetrominoThree(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_height()):
            rect = (self._start_x + self._size, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x, self._start_y + self._size, self._size, self._size)
        self.add_rectangle(rect)


class TtetrominoFour(Tetromino):
    _square_tetromino = []
    _index_height = 3
    _index_width = 2

    def create_tetromino(self):
        self.delete_tetromino()
        for i in range(self.get_index_height()):
            rect = (self._start_x + self._size, self._start_y + i * self._size, self._size, self._size)
            self.add_rectangle(rect)
        rect = (self._start_x +self.get_size()*2, self._start_y + self._size, self._size, self._size)
        self.add_rectangle(rect)



