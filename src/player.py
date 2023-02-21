from .constants import *
from .monster import Creature, creatures
from .cave import random_location

def init_player(mmap):
    """ Initialize creature list with player as 1st element """
    player = Creature('player', y_pos, x_pos, '@')
    x_pos, y_pos = random_location(mem_map)
    player.set_x_pos(x_pos)
    player.set_y_pos(y_pos)
    player.set_player(True)

    # Hur göra?
    creatures = []
    creatures.append(player)
    game_data.set_creatures(creatures)
    src.maps.update_creatures(game_data)
    win.refresh()
    return creatures
    
