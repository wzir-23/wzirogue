''' Functions for generating caves '''
import random

# game screen dimensions
WIDTH = 80
HEIGHT = 25
# parameters for cave generator
MAX_ROOMS = 8
ROOM_MIN_WIDTH = 6
ROOM_MIN_HEIGHT = 4
ROOM_MAX_WIDTH = 16
ROOM_MAX_HEIGHT = 9

def create_room(cave, room):
    """ plot room in cave """
    for row in range(room[1], room[1] + room[3]):
        for col in range(room[0], room[0] + room[2]):
            # print(f'cave[row][col]: {row:},{col}  - room: {room}')
            if (col == room[0] or (col == room[0] + room[2] - 1)):  # walls?
                cave[row][col] = '|'
            else:
                cave[row][col] = '.'
            if (row == room[1] or (row == room[1] + room[3] - 1)):  # floor/ceiling?
                cave[row][col] = '-'
    # print(room)


def dig_cave():
    ''' starts with empty cave and populates it with rooms '''
    rooms = []
    cave = [[' ' for col in range(0, WIDTH)] for row in range(0, HEIGHT)]
    # Screen dimensions of 80x25 characters are divided into nine fields, each
    # 8 characters high and 26 characters wide, leaving one row for the status
    # bar and one wasted character on the each side
    for h_field in [0, 1, 2]:
        min_y = h_field * 8 + 1
        max_y = h_field * 8 + 8
        for v_field in [0, 1, 2]:
            min_x = v_field * 26 + 1
            max_x = v_field * 26 + 26
            # we need the rooms to be at least 4 characters heigh and 6
            # characters wide
            x = random.randrange(min_x, max_x - 6)
            y = random.randrange(min_y, max_y - 4)
            w = random.randrange(x + 6, max_x) - x
            h = random.randrange(y + 4, max_y) - y
            new_room = [x, y, w, h]
            rooms.append(new_room)
            print(f'{h_field}:{v_field} -  x: {x}, y: {y}, w: {w}, h: {h}')
            create_room(cave, new_room)
    return cave, rooms
