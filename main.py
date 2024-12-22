import pygame
from tetrominoes import (Itetromino,
                         Otetromino,
                         Ltetromino,
                         SIZE, SCALE,
                         )
pygame.font.init()


WIDTH, HEIGHT = SIZE*SCALE*1.29, SIZE*10

GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT = WIDTH - (SIZE * (WIDTH/SIZE)*0.3), HEIGHT
PRE_GAME_WIDTH, PRE_GAME_HEIGHT = WIDTH-GAME_FIELD_WIDTH, HEIGHT*0.4

GAME_FIELD_COLOR = (71,70,68)
PRE_GAME_FIELD_COLOR = (222, 209, 175)
SQUARE_COLOR = (0, 119, 255)
RECTANGLE_IN_THE_FIELD_COLOR = (47, 235, 213)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

list_of_tetromino_in_the_field = []
list_of_rectangle_in_the_field = []




def draw_window(game_field,
                field_squares,
                pre_game_field,
                o_tetromino
                ):

    WINDOW.fill((0, 0, 0))

    pygame.draw.rect(WINDOW, GAME_FIELD_COLOR, game_field)
    pygame.draw.rect(WINDOW, PRE_GAME_FIELD_COLOR, pre_game_field)

    for square in field_squares:
        pygame.draw.rect(WINDOW, SQUARE_COLOR, square,1)

    for rectangle in list_of_rectangle_in_the_field:
        pygame.draw.rect(WINDOW, RECTANGLE_IN_THE_FIELD_COLOR, rectangle)

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


def tetromino_not_in_tetromino(tetromino):

    for rectangle in list_of_rectangle_in_the_field:
        if tetromino.start_x + tetromino.size*2 > rectangle[0] > tetromino.start_x and \
             tetromino.start_y + tetromino.size*2 > rectangle[1] > tetromino.start_y or \
             tetromino.start_x + tetromino.size*2 > rectangle[0]+SIZE > tetromino.start_x and \
             tetromino.start_y + tetromino.size*2 > rectangle[1] > tetromino.start_y or \
             tetromino.start_x + tetromino.size*2 > rectangle[0]+SIZE  > tetromino.start_x and \
             tetromino.start_y + tetromino.size*2 > rectangle[1]+SIZE > tetromino.start_y or \
             tetromino.start_x + tetromino.size*2 > rectangle[0] > tetromino.start_x and \
             tetromino.start_y + tetromino.size*2 > rectangle[1]+SIZE > tetromino.start_y:
            return False
    return True


def tetromino_in_the_field(tetromino):

    for rectangle in list_of_rectangle_in_the_field:
        if len(list_of_rectangle_in_the_field) > 0:
            if (tetromino.start_x == rectangle[0] and
                    tetromino.start_y == rectangle[1] and
                    tetromino.start_x < GAME_FIELD_WIDTH):
                return True
    return False


def tetromino_within_window(o_tetromino):

    if o_tetromino.start_x < 0 or \
        o_tetromino.start_y < 0  or \
        o_tetromino.start_x+o_tetromino.size*2 > WIDTH or \
        o_tetromino.start_y+o_tetromino.size*2 > HEIGHT or \
            not pygame.mouse.get_focused():
        return False
    return True


def stick_tetromino_to_square(list_of_rect):

    size = list_of_rect[0][2]*0.99
    for index, rectangle in enumerate(list_of_rect):
        rectangle_x = round(rectangle[0]/size)*size*1.05
        rectangle_y = round(rectangle[1]/size)*size*1.05
        list_of_rectangle_in_the_field.append((rectangle_x, rectangle_y, size, size))


def move_tetromino(event_start_x, event_start_y, o_tetromino):

    o_tetromino.square_O_tetromino.clear()
    if tetromino_within_window(o_tetromino):
        o_tetromino.start_x = o_tetromino.start_x + event_start_x
        o_tetromino.start_y = o_tetromino.start_y + event_start_y
    else:
        o_tetromino.start_x = o_tetromino.start_x - event_start_x * 2
        o_tetromino.start_y = o_tetromino.start_y - event_start_y * 2
    o_tetromino.square_O_tetromino.clear()
    o_tetromino.draw_Otetromino(WINDOW)


def drop_tetromino(o_tetromino, mouse_in_rect):

    if mouse_in_rect and o_tetromino.start_x+SIZE*2*0.98 < GAME_FIELD_WIDTH*1.01:
        list_of_tetromino_in_the_field.append(o_tetromino.square_O_tetromino[:4])
        stick_tetromino_to_square(o_tetromino.square_O_tetromino[:4])

    o_tetromino.square_O_tetromino.clear()
    o_tetromino.start_x = SIZE * SCALE
    o_tetromino.start_y = SIZE
    o_tetromino.draw_Otetromino(WINDOW)


def main():
    clock = pygame.time.Clock()
    run = True

    game_field = pygame.Rect(0, 0, GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT)
    pre_game_field = pygame.Rect(GAME_FIELD_WIDTH, 0, PRE_GAME_WIDTH, PRE_GAME_HEIGHT)

    field_squares = [square for square in create_square()]

    o_tetromino = Otetromino()
    pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_in_rect = mouse_in_rectangle(mouse_x, mouse_y, o_tetromino.square_O_tetromino)

            if pygame.mouse.get_pressed()[0] and not tetromino_in_the_field(o_tetromino):
                event_start_x, event_start_y = pygame.mouse.get_rel()

                if event.type == pygame.MOUSEMOTION and mouse_in_rect  and abs(event_start_x) < 70 and abs(event_start_y) < 70:

                    move_tetromino(event_start_x, event_start_y, o_tetromino)

            elif (event.type == pygame.MOUSEBUTTONUP and
                    not tetromino_in_the_field(o_tetromino) and
                    tetromino_not_in_tetromino(o_tetromino)):

                drop_tetromino(o_tetromino, mouse_in_rect)

        draw_window(
            game_field,
            field_squares,
            pre_game_field,
            o_tetromino,
        )

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

