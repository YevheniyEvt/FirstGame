import pygame
pygame.font.init()

SIZE = 70
WIDTH, HEIGHT = SIZE*10, SIZE*10

GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT = WIDTH - (SIZE * (WIDTH/SIZE)*0.3), HEIGHT
PRE_GAME_WIDTH, PRE_GAME_HEIGHT = WIDTH-GAME_FIELD_WIDTH, HEIGHT

GAME_FIELD_COLOR = (71,70,68)
PRE_GAME_FIELD_COLOR = (222, 209, 175)

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60

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



def draw_window(game_field, pre_game_field, vertical_lines, horizontal_lines):

    pygame.draw.rect(WINDOW, GAME_FIELD_COLOR, game_field)
    pygame.draw.rect(WINDOW, PRE_GAME_FIELD_COLOR, pre_game_field)

    for line in vertical_lines:
        line.draw_vertical_line(WINDOW)
    for line in horizontal_lines:
        line.draw_horizontal_line(WINDOW)

    pygame.display.update()




def main():
    clock = pygame.time.Clock()
    run = True

    game_field = pygame.Rect(0, 0, GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT)
    pre_game_field = pygame.Rect(GAME_FIELD_WIDTH, 0, PRE_GAME_WIDTH, PRE_GAME_HEIGHT)


    vertical_lines = [line for line in create_vertical_lines(game_field)]
    horizontal_lines = [line for line in create_horizontal_lines(game_field)]
    print(vertical_lines)
    print(horizontal_lines)

    while run:
        clock.tick(FPS)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        draw_window(
            game_field,
            pre_game_field,
            vertical_lines,
            horizontal_lines,
        )

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

