#!/usr/bin/env python3
# coding: utf-8
""" My own rogue version """
import sys
from blessed import Terminal

import src.cave
import src.screen
from src.constants import HEIGHT, WIDTH


def init_mem_map():
    ''' initialize a memory representation of all map objects '''
    mem_map = [[src.cave.Tile() for x in range(WIDTH)] for y in range(HEIGHT)]
    return mem_map


def main():
    """ Main function """
    term = src.screen.init_terminal()
    if term == False:
        sys.exit()
    print(term.home + term.clear, end='')
    src.screen.display_status(term)
    mmap = init_mem_map()
    mmap, cave = src.cave.dig_cave(mmap)
    src.screen.mem_to_term(term, mmap)
    with term.cbreak(), term.hidden_cursor():
        inp = term.inkey()
    print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))


if __name__ == '__main__':
    main()
