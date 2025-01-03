import tetrominoes
import json

size = tetrominoes.SIZE


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
                horizontal_line_10,
                ]
all_line = [
            vertical_lines,
            horizontal_lines
]
"""
horizontal: 0, 80, 161, 242, 323, 404, 485, 565, 646, 727
            0, 60, 121, 182, 243, 304, 365, 426, 487, 548
"""

def reset():
    for lines in all_line:
        for line in lines:
            line.clear()

def load_field():
    with open('save_direct/user.txt', 'r') as name:
        user = name.read()
    try:
        with open(f"save_direct/list_ractangle_{user}.txt", 'r') as list_ract:
            data = json.load(list_ract)
            list_of_rectangle = [tuple(rectangle) for rectangle in data[user]]
            return list_of_rectangle

    except FileNotFoundError:
        return []

list_of_rectangle_in_the_field = load_field()

def filling_line(list_rectangle):

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
    for line_h in horizontal_lines:
        if len(line_h) == int(tetrominoes.GAME_FIELD_WIDTH / size):
            plus_score = len(line_h)
            del_rect_in_vert(line_h)
            delete_line(line_h)
            return plus_score

    for line_v in vertical_lines:
        if len(line_v) == int(tetrominoes.GAME_FIELD_HEIGHT/size):
            plus_score = len(line_v)
            del_rect_in_horiz(line_v)
            delete_line(line_v)
            return plus_score
    return 0


def delete_line(line):
        for i in range(len(line)):
            rect = line[-1]
            line.remove(rect)
            if rect in list_of_rectangle_in_the_field:
                list_of_rectangle_in_the_field.remove(rect)


def del_rect_in_vert(line_h):
    for line in vertical_lines:
        for i in range(len(line_h)):
            if line_h[i] in line:
                line.remove(line_h[i])


def del_rect_in_horiz(line_v):
    for line in horizontal_lines:
        for i in range(len(line_v)):
            if line_v[i] in line:
                line.remove(line_v[i])