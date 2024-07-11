#!/usr/bin/env python3
# coding: utf-8
''' My own rogue version '''
import sys
from blessed import Terminal

import src.cave

# game size
WIDTH = 80
HEIGHT = 25


def check_terminal(term):
    ''' Initial terminal check '''
    if term.width < 80 or term.height < 25:
        height = term.height
        width = term.width
        print(f"Terminal window is too small ({width}, {height})")
        print("Minimum size is 80 rows / 25 lines")
        sys.exit()


def display_status(term):
    '''
    Print the status row:
    Level: 1  Gold: 0      Hp: 12(12)  Str: 16(16)  Arm: 4   Exp: 1/0
    '''
    level = 1
    gold = 0
    hitpoints = 10
    strength = 16
    armor = 4
    experience = 0
    print(term.move_xy(0, HEIGHT-1) + f'Level: {level}', end='')
    print(term.move_xy(10, HEIGHT-1) + f'Gold: {gold}', end='')
    print(term.move_xy(23, HEIGHT-1) + f'Hp: {hitpoints}', end='')
    print(term.move_xy(35, HEIGHT-1) + f'Str: {strength}', end='')
    print(term.move_xy(48, HEIGHT-1) + f'Arm: {armor}', end='')
    print(term.move_xy(57, HEIGHT-1) + f'Exp: {experience}\n', end='')


def main():
    ''' Main function '''
    term = Terminal()
    check_terminal(term)
    print(term.home + term.clear)
    display_status(term)
    dungeon, rooms = src.cave.dig_cave()
    for row in range (0, HEIGHT):
        for col in range (0, WIDTH):
            print(term.move_xy(col, row - 1) + dungeon[row][col], end='')
    with term.cbreak(), term.hidden_cursor():
        # term.location(0, term.height - 1)
        # print(term.black_on_darkkhaki(term.center('tokfrans any key to continue.')))
        inp = term.inkey()
    print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp)))

if __name__ == '__main__':
    main()
