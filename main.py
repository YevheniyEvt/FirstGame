import pygame
from tetrominoes import (Itetromino,
                         Otetromino,
                         Ltetromino,
                         SIZE,
                         )
pygame.font.init()


WIDTH, HEIGHT = SIZE*10*1.29, SIZE*10

GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT = WIDTH - (SIZE * (WIDTH/SIZE)*0.3), HEIGHT
PRE_GAME_WIDTH, PRE_GAME_HEIGHT = WIDTH-GAME_FIELD_WIDTH, HEIGHT

GAME_FIELD_COLOR = (71,70,68)
PRE_GAME_FIELD_COLOR = (222, 209, 175)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

list_of_termino_in_the_field = []

class Line:
    size = SIZE

    def __init__(self, x, y, color, width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw_vertical_line(self, window):
        pygame.draw.line(window, self.color,
                         (self.x + self.size, self.y),
                         (self.x +self.size, self.y + HEIGHT),
                         self.width)

    def draw_horizontal_line(self, window):
        pygame.draw.line(window, self.color,
                         (self.x, self.y + self.size),
                         (self.x + GAME_FIELD_WIDTH, self.y + self.size),
                         self.width)

    def change_x(self):
        self.x += self.size

    def change_y(self):
        self.y += self.size


def create_vertical_lines(game_field):
    colum_number = int(game_field.width/SIZE)
    x = 0
    for number in range(colum_number):
        line = Line(x, 0, (102, 99, 89), 2)
        x += line.size
        yield line

def create_horizontal_lines(game_field):
    row_number = int(game_field.height/SIZE)
    y = 0
    for number in range(row_number):
        line = Line(0, y, (102, 99, 89), 2)
        y += line.size
        yield line


def draw_window(game_field,
                pre_game_field,
                vertical_lines,
                horizontal_lines,
                field_squers,
                o_tetromino,
                ):
    WINDOW.fill((0, 0, 0))

    color = (163, 181, 49)
    pygame.draw.rect(WINDOW, GAME_FIELD_COLOR, game_field)
    #pygame.draw.rect(WINDOW, PRE_GAME_FIELD_COLOR, pre_game_field,)

    for line in vertical_lines:
        line.draw_vertical_line(WINDOW)
    for line in horizontal_lines:
        line.draw_horizontal_line(WINDOW)
# приховати квадрати кольором екрану або намалювати їх позаду
    for squre in field_squers:
        pygame.draw.rect(WINDOW, color, squre,1)

    #"""Зробити випадковий вибір зі списка можливих фігур"""

    for termino in list_of_termino_in_the_field:
        for rectangle in termino:
            pygame.draw.rect(WINDOW, o_tetromino.color, rectangle)

    # for rectangle in o_tetromino.square_O_tetromino:
    #     pygame.draw.rect(WINDOW, o_tetromino.color, rectangle)
    #     print(o_tetromino.square_O_tetromino)
    o_tetromino.draw_Otetromino(WINDOW)
    pygame.display.update()

def create_square():
    size = SIZE
    start_x = 0
    start_y = 0
    for i in range(int(GAME_FIELD_WIDTH/size)):
        for j in range(int(GAME_FIELD_HEIGHT/size)):
            square = pygame.rect.Rect(start_x+i*size, start_y + j*size, size, size)
            yield square

def mouse_in_rectangle(mouse_x, mouse_y, rectangles):
    for rectangle in rectangles:
        rectangle_x = rectangle[0]
        rectangle_y = rectangle[1]
        rectangle_width = rectangle[2]
        rectangle_height = rectangle[3]
        if (rectangle_x+rectangle_width*1.5 > mouse_x > rectangle_x-rectangle_width*0.5
                and rectangle_y+rectangle_height*1.5 > mouse_y > rectangle_y-rectangle_height*0.5):
            return True
    return False



def tetromino_in_the_field(o_tetromino, mouse_x, mouse_y):
    for termino in list_of_termino_in_the_field:
        print(list_of_termino_in_the_field)
        if len(list_of_termino_in_the_field) > 0:
            if (o_tetromino.start_x == termino[0][0] and
                    o_tetromino.start_y == termino[0][1] and
                    o_tetromino.start_x < GAME_FIELD_WIDTH):
                return True
            # elif mouse_in_rectangle(mouse_x, mouse_y, termino):
            #     return True
    return False

def main():
    clock = pygame.time.Clock()
    run = True

    game_field = pygame.Rect(0, 0, GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT)
    pre_game_field = pygame.Rect(GAME_FIELD_WIDTH, 0, PRE_GAME_WIDTH, PRE_GAME_HEIGHT)

    vertical_lines = [line for line in create_vertical_lines(game_field)]
    horizontal_lines = [line for line in create_horizontal_lines(game_field)]
    field_squers = [squre for squre in create_square()]

    o_tetromino = Otetromino()
    pygame.display.update()
    while run:
        clock.tick(FPS)
        #print(list_of_termino_in_the_field)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #print(f"Фігура: {o_tetromino.square_O_tetromino}")
            # print(f"фігура в списку на  полі: {list_of_termino_in_the_field}")
            # print(f"на  полі: {len(list_of_termino_in_the_field)}")

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] and not tetromino_in_the_field(o_tetromino, mouse_x, mouse_y):

                event_start_x, event_start_y = pygame.mouse.get_rel()
                print(f"x: {event_start_x}, y: {event_start_y}")
                mouse_in = mouse_in_rectangle(mouse_x, mouse_y, o_tetromino.square_O_tetromino)
                if event.type == pygame.MOUSEMOTION and mouse_in and abs(event_start_x) < 100 and abs(event_start_y) < 100:
                    o_tetromino.square_O_tetromino.clear()

                    o_tetromino.start_x = o_tetromino.start_x + event_start_x
                    o_tetromino.start_y = o_tetromino.start_y + event_start_y
                    o_tetromino.square_O_tetromino.clear()
                    o_tetromino.draw_Otetromino(WINDOW)

            elif event.type == pygame.MOUSEBUTTONUP and not tetromino_in_the_field(o_tetromino, mouse_x, mouse_y) and o_tetromino.start_x+SIZE*2 < GAME_FIELD_WIDTH:
                if mouse_in:
                    list_of_termino_in_the_field.append(o_tetromino.square_O_tetromino[:4])
                o_tetromino.square_O_tetromino.clear()
                o_tetromino.start_x = SIZE * 10
                o_tetromino.start_y = SIZE
                o_tetromino.draw_Otetromino(WINDOW)

        draw_window(
            game_field,
            pre_game_field,
            vertical_lines,
            horizontal_lines,
            field_squers,
            o_tetromino,
        )

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

# потрібно зробити обмеження щоб не виходив за екран, зробити нормальне обмеження по переміщенню.
# додати зміну координат в клас
# зробити прилоипання до координат клітинок

