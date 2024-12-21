import pygame


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

                event_start_x, event_start_y = pygame.mouse.get_rel()
                if event.type == pygame.MOUSEMOTION:

                    start_x = start_x + event_start_x
                    start_y = start_y + event_start_y

        draw()
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()