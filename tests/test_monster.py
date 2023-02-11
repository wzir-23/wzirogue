import unittest
from src import monster

class TestCreatureClass(unittest.TestCase):
    ''' Test Creature class '''
    def test_update_xy_pos(self):
        ork = monster.Creature('WAAAGH', 0, 0, 'O')
        ork.set_xpos(40)
        ork.set_ypos(12)
        x_pos = ork.get_xpos()
        y_pos = ork.get_ypos()
        self.assertEqual(x_pos, 40)
        self.assertEqual(y_pos, 12)

    def test_name_and_char(self):
        ork = monster.Creature('Warboss', 0, 0, 'O')
        name = ork.get_name()
        char = ork.get_char()
        self.assertEqual(name, 'Warboss')
        self.assertEqual(char, 'O')

    def test_is_player(self):
        ork = monster.Creature('WAAAGH', 0, 0, 'O')
        ork.set_player(True)
        is_player = ork.get_player()
        self.assertTrue(is_player)
