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




def draw_field(game_field):
    line = Line(0,0,(102, 99, 89), 2)
    lines = []
    colum_number = int(game_field.width/line.size)
    row_number = int(game_field.height/line.size)

    for number in range(colum_number):
        line.draw_vertical_line(WINDOW)
        line.change_x()
    line.x = 0

    for number_2 in range(row_number):
        line.draw_horizontal_line(WINDOW)
        line.y += SIZE


def draw_window(game_field, pre_game_field):
    pygame.draw.rect(WINDOW, GAME_FIELD_COLOR, game_field)
    pygame.draw.rect(WINDOW, PRE_GAME_FIELD_COLOR, pre_game_field)

def main():
    clock = pygame.time.Clock()
    run = True

    game_field = pygame.Rect(0,0,GAME_FIELD_WIDTH,GAME_FIELD_HEIGHT)
    pre_game_field = pygame.Rect(GAME_FIELD_WIDTH, 0, PRE_GAME_WIDTH,PRE_GAME_HEIGHT)


    while run:
        clock.tick(FPS)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            run = False
            break

        draw_window(game_field, pre_game_field)
        draw_field(game_field)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

