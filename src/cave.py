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
            if (row == room[1] or (row == room[1] + room[3] - 1)):  # floor/ceiling?
                cave[row][col] = '#'
            else:
                if (col == room[0] or (col == room[0] + room[2] - 1)):  # walls?
                    cave[row][col] = '#'
                else:
                    cave[row][col] = '.'


def box_overlap(a, b):
    """ Determine if two boxes intersect """
    # Box A left corner is to the right of Box B right corner or
    # Box B left corner is to the right of Box A right corner
    # Boxes don't overlap in the x axis
    if a[0] > (b[0] + b[2]) or b[0] > (a[0] + a[2]):
        return False
    # Boxes don't overlap in the y axis
    if b[1] > (a[1] + a[3]) or a[1] > (b[1] + b[3]):
        return False
    return True


def dig_cave():
    rooms = []
    cave = [[' ' for col in range(0, WIDTH)] for row in range(0, HEIGHT)]
    num_rooms = random.randrange(4, MAX_ROOMS)

    while num_rooms:
        not_done = 0
        failed = False

        # Try creating a room with random coordinates
        w = random.randrange(ROOM_MIN_WIDTH, ROOM_MAX_WIDTH)
        h = random.randrange(ROOM_MIN_HEIGHT, ROOM_MAX_HEIGHT)
        x = random.randrange(0, WIDTH  - 1 - w)
        y = random.randrange(0, HEIGHT - 1 - h)
        new_room = [x, y, w, h]

        if len(rooms):
            for room in rooms:
                if box_overlap(new_room, room):
                    failed = True

        if not failed:
            print(f'room - x: {x}, y: {y}, w: {w}, h: {h}')
            create_room(cave, new_room)
            rooms.append(new_room)
            num_rooms -= 1
    return cave, rooms
