''' Let there be monsters (and players) '''

creatures = []

class Creature():
    ''' monster/hero class '''
    global creatures
    def __init__(self, name, xpos, ypos, char):
        self.name = name
        self.xpos = xpos
        self.ypos = 'ypos
        self.char = char
        self.player = False
        creatures.append(self)
    def get_char(self):
        ''' get character representation '''
        return self.char
    def set_xpos(self, xpos):
        ''' set x position '''
        self.xpos = xpos
    def set_ypos(self, ypos):
        ''' set y position '''
        self.ypos = ypos
    def get_xpos(self, xpos):
        ''' get x position '''
        return self.xpos
    def get_ypos(self, ypos):
        ''' get y position '''
        return self.ypos
    def set_player(self):
        ''' true if hero, false if monster '''
        self.player = True
    def get_player(self):
        ''' return hero/monster object '''
        return self.player
