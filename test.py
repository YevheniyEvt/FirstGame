import pygame
import time
import tetrominoes
# class Line:
#     size = SIZE
#
#     def __init__(self, x, y, color, width):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = width
#
#     def draw_vertical_line(self, window):
#         pygame.draw.line(window, self.color,
#                          (self.x + self.size, self.y),
#                          (self.x +self.size, self.y), # + HEIGHT),
#                          self.width)
#
#     def draw_horizontal_line(self, window):
#         pygame.draw.line(window, self.color,
#                          (self.x, self.y + self.size),
#                          (self.x + GAME_FIELD_WIDTH, self.y + self.size),
#                          self.width)
#
#     def change_x(self):
#         self.x += self.size
#
#     def change_y(self):
#         self.y += self.size

#
# def create_vertical_lines(game_field):
#     colum_number = int(game_field.width/SIZE)
#     x = 0
#     for number in range(colum_number):
#         line = Line(x, 0, (102, 99, 89), 2)
#         x += line.size
#         yield line
#
# def create_horizontal_lines(game_field):
#     row_number = int(game_field.height/SIZE)
#     y = 0
#     for number in range(row_number):
#         line = Line(0, y, (102, 99, 89), 2)
#         y += line.size
#         yield line


window = pygame.display.set_mode((700,700))
size = 60
start_x = size*5
start_y = size 

def draw():
    window.fill((0, 0, 0))

    for i in range(2):
        rect = (start_x + i * size, start_y, size, size)
        pygame.draw.rect(window, 'blue', rect)
    for i in range(2):

        rect = (start_x + i * size, start_y + size, size, size)
        pygame.draw.rect(window, 'blue', rect)

def main():
    clock = pygame.time.Clock()
    global start_x
    global start_y
    run = True
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0]:  # and not tetromino_in_the_field(o_tetromino, mouse_x, mouse_y):
                pygame.mouse.set_visible(0)
                event_start_x, event_start_y = pygame.mouse.get_rel()
                if event.type == pygame.MOUSEMOTION:

                    start_x = start_x + event_start_x
                    start_y = start_y + event_start_y
            else:pygame.mouse.set_visible(1)

        draw()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()


