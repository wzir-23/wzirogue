""" Cave related functions """

import random
from .constants import *


class Tile():
    ''' The smallest building block in a map '''
    def __init__(self):
        self.tile = ' '
        self.visible = True
    def get(self):
        ''' return tile object '''
        return self.tile
    def set(self, item):
        ''' set  tile object '''
        self.tile = item
    def set_visible(self, shown):
        ''' true/false if visible/hidden '''
        self.visible = shown
    def get_visible(self):
        ''' is visible/hidden '''
        return self.visible


def create_room(cave, room):
    """ plot walled room in cave """
    for row in range(room[1], room[1] + room[3]):
        for col in range(room[0], room[0] + room[2]):
            if (col == room[0] or (col == room[0] + room[2] - 1)):
                cave[row][col] = '|'
            else:
                cave[row][col] = '.'
            if (row == room[1] or (row == room[1] + room[3] - 1)):
                cave[row][col] = '-'


def box_overlap(box_a, box_b):
    """ Determine if two boxes intersect """
    # Box A left corner is to the right of Box B right corner or
    # Box B left corner is to the right of Box A right corner
    # Boxes don't overlap in the x axis
    if box_a[0] > (box_b[0] + box_b[2]) or box_b[0] > (box_a[0] + box_a[2]):
        return False
    # Boxes don't overlap in the y axis
    if box_b[1] > (box_a[1] + box_a[3]) or box_a[1] > (box_b[1] + box_b[3]):
        return False
    return True


def cave_to_mem(mmap, cave):
    ''' copy rooms to memory map '''
    for row in range(0, HEIGHT):
        for col in range(0, WIDTH):
            mmap[row][col].set(cave[row][col])
    return mmap


def dig_cave(mmap):
    """ Dig random number of rooms """
    rooms = []
    cave = [[' ' for col in range(0, WIDTH)] for row in range(0, HEIGHT)]
    num_rooms = random.randrange(4, MAX_ROOMS)
    while num_rooms:
        failed = False
        # Try creating a room with random coordinates
        room_w = random.randrange(ROOM_MIN_WIDTH, ROOM_MAX_WIDTH)
        room_h = random.randrange(ROOM_MIN_HEIGHT, ROOM_MAX_HEIGHT)
        room_x = random.randrange(0, WIDTH  - 1 - room_w)
        room_y = random.randrange(0, HEIGHT - 1 - room_h)
        new_room = [room_x, room_y, room_w, room_h]
        if len(rooms) > 0:
            for room in rooms:
                if box_overlap(new_room, room):
                    failed = True
        if not failed:
            print(f'room - x: {room_x}, y: {room_y}, w: {room_w}, h: {room_h}')
            create_room(cave, new_room)
            rooms.append(new_room)
            num_rooms -= 1
    mmap = cave_to_mem(mmap, cave)
    return mmap, cave
