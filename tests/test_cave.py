import unittest
from src import cave

class TestTileClass(unittest.TestCase):
    ''' Test Tile class '''
    def test_tile(self):
        tile = cave.Tile()
        tile_char = tile.get()
        self.assertEqual(tile_char, ' ')

    def test_visible(self):
        tile = cave.Tile()
        visible = tile.get_visible()
        self.assertTrue(visible)
        tile.set_visible(False)
        invisible = tile.get_visible()
        self.assertFalse(invisible)
