from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes

import main
import tetrominoes
pygame.init()

width = tetrominoes.WIDTH
heigth = tetrominoes.HEIGHT
window = pygame.display.set_mode((width, heigth))


def set_difficulty(value, difficulty):
    with open("save_direct/dificult.txt", 'w') as file:
        file.write(str(difficulty))


def start_the_game():
    main.main()

def level_menu():
    mainmenu._open(level)



def text(text):
    with open("save_direct/user.txt", 'w') as file:
        file.write(str(text))


mainmenu = pygame_menu.Menu("Tetromino", width, heigth, theme=themes.THEME_DARK)
mainmenu.add.text_input("Name: ", maxchar=20, onchange=text)
mainmenu.add.button("Start Game", start_the_game)
mainmenu.add.button("Levels", level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu("select Difficulty", width, heigth, theme=themes.THEME_DARK)
level.add.selector("Difficulty: ",[("Hard",1),("Easy",2)], onchange=set_difficulty)

def menu():
    mainmenu.mainloop(window)

if __name__ == '__main__':
    menu()

