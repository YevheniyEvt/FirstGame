import random
import time
import pygame
import tetrominoes
import rectangleInField
from tetrominoes import (Itetromino, ItetrominoTwo, Otetromino, Stetromino, StetrominoTwo, StetrominoThree,
    StetrominoFour, Ltetromino, LtetrominoTwo, Jtetromino, JtetrominoTwo, JtetrominoThree, JtetrominoFour, Ttetromino)

pygame.font.init()




SIZE = tetrominoes.SIZE
SCALE = tetrominoes.SCALE
WIDTH, HEIGHT = tetrominoes.WIDTH, tetrominoes.HEIGHT

GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT = tetrominoes.GAME_FIELD_WIDTH, tetrominoes.GAME_FIELD_HEIGHT
PRE_GAME_WIDTH, PRE_GAME_HEIGHT = tetrominoes.PRE_GAME_WIDTH, tetrominoes.PRE_GAME_HEIGHT
SCORE_FIELD_WIDTH, SCORE_FIELD_HEIGHT = tetrominoes.SCORE_FIELD_WIDTH, tetrominoes.SCORE_FIELD_HEIGHT



GAME_FIELD_COLOR = (71,70,68)
PRE_GAME_FIELD_COLOR = (11, 176, 217)
SQUARE_COLOR = (0, 119, 255)
RECTANGLE_IN_THE_FIELD_COLOR = (252, 186, 3)
SCORE_FIELD_COLOR = (71,70,68)

WINDOW = tetrominoes.WINDOW
FPS = 60

size_font = int(SIZE*0.7)
FONT = pygame.font.SysFont('comicsans' ,size_font)

list_of_tetromino_in_the_field = []
list_of_rectangle_in_the_field = rectangleInField.list_of_rectangle_in_the_field

clas_tetromino = [Itetromino(), ItetrominoTwo(), Otetromino(), Stetromino(), StetrominoTwo(), StetrominoThree(),
                StetrominoFour(), Ltetromino(), LtetrominoTwo(), Jtetromino(), JtetrominoTwo(), JtetrominoThree(), JtetrominoFour(), Ttetromino()]


def draw_window(game_field,
                field_squares,
                pre_game_field,
                tetromino,
                score_total, score_field,
                ):

    pygame.draw.rect(WINDOW, GAME_FIELD_COLOR, game_field)
    pygame.draw.rect(WINDOW, PRE_GAME_FIELD_COLOR, pre_game_field)

    for square in field_squares:
        pygame.draw.rect(WINDOW, SQUARE_COLOR, square,1)

    for rectangle in list_of_rectangle_in_the_field:
        pygame.draw.rect(WINDOW, RECTANGLE_IN_THE_FIELD_COLOR, rectangle)

    score(score_total, score_field)

    tetromino.draw_tetromino(WINDOW)
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


def tetromino_not_in_tetromino(tetromino):

    for rectangle in list_of_rectangle_in_the_field:
        for tetromino_rect in tetromino.get_square():
            if tetromino_rect[0] + tetromino_rect[2]  > rectangle[0] > tetromino_rect[0] and \
                 tetromino_rect[1] + tetromino_rect[2] > rectangle[1] > tetromino_rect[1] or \
                 tetromino_rect[0] + tetromino_rect[2] > rectangle[0]+tetromino_rect[2] > tetromino_rect[0] and \
                 tetromino_rect[1] + tetromino_rect[2] > rectangle[1] > tetromino_rect[1] or \
                 tetromino_rect[0] + tetromino_rect[2] > rectangle[0]+tetromino_rect[2]  > tetromino_rect[0] and \
                 tetromino_rect[1] + tetromino_rect[2] > rectangle[1]+tetromino_rect[2] > tetromino_rect[1] or \
                 tetromino_rect[0] + tetromino_rect[2] > rectangle[0] > tetromino_rect[0]and \
                 tetromino_rect[1] + tetromino_rect[2] > rectangle[1]+tetromino_rect[2] > tetromino_rect[1]:
                return False
    return True


def tetromino_in_the_field(tetromino):

    for rectangle in list_of_rectangle_in_the_field:
        if len(list_of_rectangle_in_the_field) > 0:
            if (tetromino.get_start_x() == rectangle[0] and
                    tetromino.get_start_y() == rectangle[1] and
                    tetromino.get_start_x() < GAME_FIELD_WIDTH):
                return True
    return False


def tetromino_within_window(tetromino):

    for tetromino_rect in tetromino.get_square():
        if tetromino_rect[0] < 0.5:
            tetromino.set_start_x(tetromino.get_start_x()+0.5)
            return False
        elif tetromino_rect[1] < 0.5:
            tetromino.set_start_y(tetromino.get_start_y()+0.5)
            return False
        elif tetromino_rect[0] + tetromino.get_size() > (WIDTH-0.5):
            tetromino.set_start_x(tetromino.get_start_x()-0.5)
            return False
        elif tetromino_rect[1] + tetromino.get_size() > (HEIGHT-0.5):
            tetromino.set_start_y(tetromino.get_start_y()-0.5)
            return False

    return True

def stick_tetromino_to_square(tetromino):

    size = round(tetromino.get_square()[0][2])
    if tetromino.get_start_x() >= 0 and tetromino.get_start_y() >= 0:
        for rectangle in tetromino.get_square():
            rectangle_x = int(rectangle[0]/size)*size*1.04
            rectangle_y = int(rectangle[1]/size)*size*1.04
            list_of_rectangle_in_the_field.append((rectangle_x, rectangle_y, size, size))


def move_tetromino(event_start_x, event_start_y, tetromino):

    if tetromino_within_window(tetromino):
        tetromino.set_start_x(int(tetromino.get_start_x() + event_start_x))
        tetromino.set_start_y(int(tetromino.get_start_y() + event_start_y))

    tetromino.draw_tetromino(WINDOW)


def drop_tetromino(tetromino, mouse_in_rect):

    if (mouse_in_rect and
            tetromino.get_start_x()+tetromino.get_size()*tetromino.get_index_width() < int(GAME_FIELD_WIDTH / SIZE)*SIZE*0.97 and
            tetromino.get_start_y() + tetromino.get_size()*tetromino.get_index_height() < int(GAME_FIELD_HEIGHT / SIZE)*SIZE)*0.99:

        list_of_tetromino_in_the_field.append(tetromino.get_square())
        stick_tetromino_to_square(tetromino)

    #tetromino.delete_tetromino()
    tetromino.set_start_x((SIZE * 0.97) * SCALE)
    tetromino.set_start_y(SIZE * 0.97)
    tetromino.draw_tetromino(WINDOW)

def chose_tetromino(tetrominos):
    tetromino = random.choice(tetrominos)
    #tetromino = Itetromino()
    return tetromino

def score(score_total, score_field):
    score_text = FONT.render(f"SCORE:  {score_total}", 1, 'white')
    x = GAME_FIELD_WIDTH + PRE_GAME_WIDTH//2 - score_text.get_width()//2
    y = GAME_FIELD_HEIGHT - tetrominoes.PRE_GAME_HEIGHT - score_text.get_height()//2

    pygame.draw.rect(WINDOW, SCORE_FIELD_COLOR, score_field)
    WINDOW.blit(score_text, (x, y))

def main():
    clock = pygame.time.Clock()
    run = True
    score_total = 0

    game_field = pygame.Rect(0, 0, GAME_FIELD_WIDTH*1.006, GAME_FIELD_HEIGHT)
    pre_game_field = pygame.Rect(GAME_FIELD_WIDTH*1.006, 0, PRE_GAME_WIDTH, PRE_GAME_HEIGHT)
    score_field = pygame.Rect(GAME_FIELD_WIDTH*1.006, PRE_GAME_HEIGHT, SCORE_FIELD_WIDTH, SCORE_FIELD_HEIGHT)

    field_squares = [square for square in create_square()]

    tetromino =  tetrominoes.Otetromino()
    #tetromino = random.choice(clas_tetromino)

    #pygame.display.update()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_in_rect = mouse_in_rectangle(mouse_x, mouse_y, tetromino.get_square())

            if pygame.mouse.get_pressed()[0] and not tetromino_in_the_field(tetromino) and mouse_in_rect:
                event_start_x, event_start_y = pygame.mouse.get_rel()


                #pygame.mouse.set_visible(0)

                if event.type == pygame.MOUSEMOTION  and abs(event_start_x) < 100 and abs(event_start_y) < 100:

                    move_tetromino(event_start_x, event_start_y, tetromino)

            elif (event.type == pygame.MOUSEBUTTONUP and
                    not tetromino_in_the_field(tetromino) and
                    tetromino_not_in_tetromino(tetromino)):

                drop_tetromino(tetromino, mouse_in_rect)
                #tetromino = chose_tetromino(clas_tetromino)

            # else:
            #     pygame.mouse.set_visible(1)

        score_total += rectangleInField.filling_line(list_of_rectangle_in_the_field)

        draw_window(
            game_field,
            field_squares,
            pre_game_field,
            tetromino,
            score_total, score_field,

        )

    pygame.quit()

if __name__ == "__main__":
    main()
# виправити з не вірним малюванням фігур. Початок зміщений. (КВАДРАТ)