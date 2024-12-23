import tetrominoes
import pygame


size = tetrominoes.SIZE
list_of_rectangle_in_the_field = []

vertical_line_1 = []
vertical_line_2 = []
vertical_line_3 = []
vertical_line_4 = []
vertical_line_5 = []
vertical_line_6 = []
vertical_line_7 = []
vertical_line_8 = []
vertical_line_9 = []

horizontal_line_1 = []
horizontal_line_2 = []
horizontal_line_3 = []
horizontal_line_4 = []
horizontal_line_5 = []
horizontal_line_6 = []
horizontal_line_7 = []
horizontal_line_8 = []
horizontal_line_9 = []
horizontal_line_10 = []

vertical_lines = [
                vertical_line_1,
                vertical_line_2,
                vertical_line_3,
                vertical_line_4,
                vertical_line_5,
                vertical_line_6,
                vertical_line_7,
                vertical_line_8,
                vertical_line_9,
                ]

horizontal_lines = [
                horizontal_line_1,
                horizontal_line_2,
                horizontal_line_3,
                horizontal_line_4,
                horizontal_line_5,
                horizontal_line_6,
                horizontal_line_7,
                horizontal_line_8,
                horizontal_line_9,
                horizontal_line_1,
                ]
all_Lines = [
            vertical_lines,
            horizontal_lines,
            ]
"""
horizontal: 0, 80, 161, 242, 323, 404, 485, 565, 646, 727
            0, 60, 121, 182, 243, 304, 365, 426, 487, 548
"""


def filling_line(list_rectangle):
    # for rectangle in list_rectangle:
    #     for i in range(2):
    #         for j in range(10):
    #             rect_xy = rectangle[i]
    #             if rect_xy//10 == size*j//10 and rect_xy not in all_Lines[i][j]:
    #                 all_Lines[i][j].append(rectangle)

    for rect in list_rectangle:
        if rect[0] == 0 and rect not in vertical_line_1:
            vertical_line_1.append(rect)
        elif rect[0]//10 == size//10  and rect not in vertical_line_2:
            vertical_line_2.append(rect)
        elif rect[0]//10 == size*2//10 and rect not in vertical_line_3:
            vertical_line_3.append(rect)
        elif rect[0]//10 == size*3//10 and rect not in vertical_line_4:
            vertical_line_4.append(rect)
        elif rect[0]//10 == size*4//10 and rect not in vertical_line_5:
            vertical_line_5.append(rect)
        elif rect[0]//10 == size*5//10 and rect not in vertical_line_6:
            vertical_line_6.append(rect)
        elif rect[0]//10 == size*6//10 and rect not in vertical_line_7:
            vertical_line_7.append(rect)
        elif rect[0]//10 == size*7//10 and rect not in vertical_line_8:
            vertical_line_8.append(rect)
        elif rect[0]//10 == size*8//10 and rect not in vertical_line_9:
            vertical_line_9.append(rect)

        if rect[1] == 0 and rect not in horizontal_line_1:
            horizontal_line_1.append(rect)
        elif rect[1]//10 == size //10 and rect not in horizontal_line_2:
            horizontal_line_2.append(rect)
        elif rect[1]//10 == size*2//10 and rect not in horizontal_line_3:
            horizontal_line_3.append(rect)
        elif rect[1]//10 == size*3//10 and rect not in horizontal_line_4:
            horizontal_line_4.append(rect)
        elif rect[1]//10 == size*4//10 and rect not in horizontal_line_5:
            horizontal_line_5.append(rect)
        elif rect[1]//10 == size*5//10 and rect not in horizontal_line_6:
            horizontal_line_6.append(rect)
        elif rect[1]//10 == size*6//10 and rect not in horizontal_line_7:
            horizontal_line_7.append(rect)
        elif rect[1]//10 == size*7//10 and rect not in horizontal_line_8:
            horizontal_line_8.append(rect)
        elif rect[1]//10 == size*8//10 and rect not in horizontal_line_9:
            horizontal_line_9.append(rect)
        elif rect[1]//10 == size*9//10 and rect not in horizontal_line_10:
            horizontal_line_10.append(rect)


    plus_score = check_line()
    return plus_score

def check_line():
    for line in horizontal_lines:
        if len(line) == int(tetrominoes.GAME_FIELD_WIDTH / size):
            plus_score = len(line)
            delete_line(line)
            return plus_score
    for line in vertical_lines:
        if len(line) == int(tetrominoes.GAME_FIELD_HEIGHT/size):
            plus_score = len(line)
            delete_line(line)
            return plus_score
    return 0


def delete_line(line):
        for i in range(len(line)):
            rect = line[0]
            try:
                list_of_rectangle_in_the_field.remove(rect)
                line.remove(rect)
            except ValueError:
                print(f"rect:{rect} not in {list_of_rectangle_in_the_field}")


