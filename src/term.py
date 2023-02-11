''' TUI functions '''
import sys
from .constants import HEIGHT, WIDTH

def check_terminal(term):
    ''' Initial terminal check '''
    if term.width < WIDTH or term.height < HEIGHT:
        height = term.height
        width = term.width
        print(f"Terminal window is too small ({width}, {height})")
        print("Minimum size is {WIDTH} rows / {HEIGHT} lines")
        sys.exit()


def display_status(term):
    """
    Print the status row:
    Level: 1  Gold: 0      Hp: 12(12)  Str: 16(16)  Arm: 4   Exp: 1/0
    """
    level = 1
    gold = 0
    hitpoints = 10
    strength = 16
    armor = 4
    experience = 0
    # status_bar = [0, 'Level: ', 10, 'Gold: ', 23, 'Hp: ',
                  # 35, 'Str: ', 48, 'Arm: ', 57, 'Exp: ']
    print(term.move_xy(0, HEIGHT-1) + f'Level: {level}', end='')
    print(term.move_xy(10, HEIGHT-1) + f'Gold: {gold}', end='')
    print(term.move_xy(23, HEIGHT-1) + f'Hp: {hitpoints}', end='')
    print(term.move_xy(35, HEIGHT-1) + f'Str: {strength}', end='')
    print(term.move_xy(48, HEIGHT-1) + f'Arm: {armor}', end='')
    print(term.move_xy(57, HEIGHT-1) + f'Exp: {experience}', end='')
