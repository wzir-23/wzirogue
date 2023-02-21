import unittest
from src import cave
from src.constants import WIDTH, HEIGHT


class TestTileClass(unittest.TestCase):
    ''' Test Tile class '''
    def test_get_tile(self):
        tile = cave.Tile()
        tile_char = tile.get()
        self.assertEqual(tile_char, ' ')

    def test_set_tile(self):
        tile = cave.Tile()
        tile.set('#')
        tile_char = tile.get()
        self.assertEqual(tile_char, '#')

    def test_visible(self):
        tile = cave.Tile()
        visible = tile.get_visible()
        self.assertTrue(visible)
        tile.set_visible(False)
        invisible = tile.get_visible()
        self.assertFalse(invisible)

class TestBoxOverlap(unittest.TestCase):
    ''' Test if rooms are overlapping '''
    def test_box_overlap(self):
        box_a = [ 5, 5, 15, 15]
        box_b = [ 10, 10, 5, 5]
        result = cave.box_overlap(box_a, box_b)
        self.assertTrue(True)

    def test_box_no_y_overlap(self):
        box_a = [ 0, 10, 12, 4]
        box_b = [ 10, 15, 5, 5]
        result = cave.box_overlap(box_a, box_b)
        self.assertFalse(result)

    def test_box_no_x_overlap(self):
        box_a = [ 10, 0, 4, 12]
        box_b = [ 15, 10, 5, 5]
        result = cave.box_overlap(box_a, box_b)
        self.assertFalse(result)

#class TestMiscCaveFunctions(unittest.TestCase):
#    ''' Test generic cave functions '''
    def test_cave_to_mem(self):
        mem_map = [[cave.Tile() for x in range(WIDTH)] for y in range(HEIGHT)]
        mem_list = [[ '.' for col in range(WIDTH)] for row in range(HEIGHT)]
        result = cave.cave_to_mem(mem_map, mem_list)
        self.assertEqual(result[2][2].get(), '.')
