#!/usr/bin/env python3
# coding: utf-8
""" My own rogue version """
from blessed import Terminal

import src.cave
import src.term
from src.constants import HEIGHT, WIDTH


def init_mem_map():
    ''' initialize a memory representation of all map objects '''    
    mem_map = [[src.cave.Tile() for x in range(WIDTH)] for y in range(HEIGHT)]
    return mem_map


def main():
    """ Main function """
    term = Terminal()
    src.term.check_terminal(term)
    print(term.home + term.clear, end='')
    src.term.display_status(term)
    mmap = init_mem_map()
    mmap, cave = src.cave.dig_cave(mmap)
    for row in range (0, HEIGHT):
        for col in range (0, WIDTH):
            print(term.move_xy(col, row) + cave[row][col], end='')
    with term.cbreak(), term.hidden_cursor():
        inp = term.inkey()
    print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))


if __name__ == '__main__':
    main()
